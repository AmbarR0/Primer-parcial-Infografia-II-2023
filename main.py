from objects import MenuView
import arcade

# definicion de constantes
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Gráficadora de puntos"

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AZURE_MIST)
        self.x = (SCREEN_WIDTH-300)/2 +300
        self.y = SCREEN_HEIGHT/2
        self.text = f"x: {self.x-((SCREEN_WIDTH-300)/2+300) }, y: {self.y-SCREEN_HEIGHT/2}"
        self.points = []
        self.newp = []
        self.polygons = []
        self.orderP = []
        self.m = MenuView(10, SCREEN_HEIGHT-40)
        self.time = 0.0
        self.count = 0
        self.sw = 0
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_mouse_press(self, x, y, button, modifiers):
        self.m.press(x, y)
        if self.m.point.pressed and x>300:
            if self.sw == 0:
                self.newp = []
                self.sw = 1
            self.newp.append((self.x, self.y))
            self.points.append((self.x, self.y))
            self.orderP.append((self.x, self.y))

        if self.m.drawer.pressed:
            if self.sw == 1:
                self.polygons.append(self.newp)
                self.sw = 0
        if self.m.connect.pressed:
            self.orderP.sort()
            if self.sw == 1:
                self.polygons.append(self.newp)
                self.sw = 0
        if self.m.clean.pressed:
            self.sw = 0
            self.points.clear()
            self.orderP.clear()
            self.newp.clear()
            self.polygons.clear()
    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y
        if(x>300):
            self.text = f"x: {self.x-((SCREEN_WIDTH-300)/2+300) }, y: {self.y-SCREEN_HEIGHT/2}"
    
    def on_update(self, delta_time: float):
        if self.m.connect.pressed :
            self.time += delta_time
            if self.time > 0.5 :
                self.count += 1
                self.time = 0.0


    def on_draw(self):
        arcade.start_render()
        self.m.draw()
        
        arcade.draw_text(self.text, 10, 600, arcade.color.BLACK, 20, font_name='calibri')
        arcade.draw_circle_filled(self.x, self.y, 5, arcade.color.BLUE)

        for point in self.points:
            arcade.draw_circle_filled(point[0], point[1], 5, arcade.color.COOL_BLACK)
            if self.m.watch.pressed:
                arcade.draw_text(f"({point[0]-((SCREEN_WIDTH-300)//2+300)}, {point[1]-SCREEN_HEIGHT//2})", point[0]-4, point[1]+10, arcade.color.BLACK, 10, font_name='calibri')
        
        if self.m.connect.pressed:
            arcade.draw_line_strip(self.orderP[0:self.count], arcade.color.AFRICAN_VIOLET, 3)
            if(self.count>len(self.orderP)):
                self.count = len(self.orderP)    
        else:
            self.count = 0
        
        if self.m.drawer.pressed:
            for p in self.polygons:
                arcade.draw_line_strip(p, arcade.color.AMARANTH_PINK, 3)

if __name__ == "__main__":
    app = App()
    arcade.run()