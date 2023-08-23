import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


class MenuView(arcade.View):
    def __init__ (self, x, y):
        self.point = ButtonView(550, 500, "Puntos")
        self.connect = ButtonView(500, 450, "Conectar camino de puntos")
        self.drawer = ButtonView(450, 400, "Dibujar")
        self.clean = ButtonView(400, 350, "Limpiar")
        self.watch = ButtonView(350, 300, "Mostrar coordenadas")

        self.x = x
        self.y = y


    def draw(self):
        arcade.draw_lrtb_rectangle_filled(0,300,SCREEN_HEIGHT,0, arcade.color.BEAU_BLUE)
        arcade.draw_lrtb_rectangle_outline(0,300,SCREEN_HEIGHT,0, arcade.color.COOL_BLACK, 5)
        arcade.draw_triangle_filled(990, 344, 990, 358, SCREEN_WIDTH+2, 350, arcade.color.TEA_GREEN)
        arcade.draw_triangle_filled(312, 344, 312, 358, 301, 350, arcade.color.TEA_GREEN)
        arcade.draw_triangle_filled(642, 10, 658, 10, 650, -2, arcade.color.TEA_ROSE)
        arcade.draw_triangle_filled(642, SCREEN_HEIGHT-10, 658, SCREEN_HEIGHT-10, 650, SCREEN_HEIGHT+2, arcade.color.TEA_ROSE)
        arcade.draw_text("y", 658, SCREEN_HEIGHT-20, arcade.color.RED_DEVIL, 16, font_name='calibri')
        arcade.draw_text("-y", 658, 5, arcade.color.RED_DEVIL, 16, font_name='calibri')
        arcade.draw_text("x", 984, 360, arcade.color.GREEN, 16, font_name='calibri')
        arcade.draw_text("-x", 310, 360, arcade.color.GREEN, 16, font_name='calibri')

        arcade.draw_text("Graficadora de puntos :D", self.x, self.y, arcade.color.BLACK, 20, font_name='calibri')
        arcade.draw_line(302,SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT/2, arcade.color.TEA_GREEN, 3)
        arcade.draw_line((SCREEN_WIDTH-300)/2 +300 ,0, (SCREEN_WIDTH-300)/2 +300, SCREEN_HEIGHT, arcade.color.TEA_ROSE, 3)
        self.point.draw()
        self.connect.draw()
        self.drawer.draw()
        self.clean.draw()
        self.watch.draw()
   

    def press(self, x, y):
        if 0 <= x <= 300:
            if 500 < y < 550:
                self.point.pressed = True
                self.connect.pressed = False
                self.drawer.pressed = False
                self.clean.pressed = False

            elif 450 < y < 500:
                self.point.pressed = False
                self.connect.pressed = True
                self.drawer.pressed = False
                self.clean.pressed = False

            elif 400 < y < 450:
                self.point.pressed = False
                self.connect.pressed = False
                self.drawer.pressed = True
                self.clean.pressed = False
            elif 350 < y < 400:
                self.point.pressed = False
                self.connect.pressed = False
                self.drawer.pressed = False
                self.clean.pressed = True
            
            if 300 < y <350:
                if self.watch.pressed:
                    self.watch.pressed = False
                else:
                    self.watch.pressed = True

                
       

class ButtonView(arcade.View):
    def __init__ (self, y1, y2, text):
        self.y1 = y1
        self.y2 = y2
        self.text = text
        self.pressed = False
    def draw(self):
        
        if self.pressed:
            arcade.draw_lrtb_rectangle_filled(4,296,self.y1,self.y2, arcade.color.COOL_BLACK)
            arcade.draw_lrtb_rectangle_outline(4,296,self.y1,self.y2, arcade.color.COOL_BLACK, 5)
            arcade.draw_text(self.text, 150, (self.y1+self.y2)//2, arcade.color.WHITE, font_size=20, anchor_x="center",anchor_y="center", font_name="calibri")

        else:
            arcade.draw_lrtb_rectangle_filled(4,296,self.y1,self.y2, arcade.color.BEAU_BLUE)
            arcade.draw_lrtb_rectangle_outline(4,296,self.y1,self.y2, arcade.color.BEAU_BLUE, 1)
            arcade.draw_text(self.text, 150, (self.y1+self.y2)//2, arcade.color.BLACK, font_size=20, anchor_x="center",anchor_y="center", font_name="calibri")

