import arcade

Direction = {"North","South","East","West"}
class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.sprite_image = None
        self.x = None
        self.y = None
        self.direction = None
        self.bounce = 0

    def setup(self, src, initial_x,initial_y):
        self.sprite_image = src
        self.x = initial_x
        self.y = initial_y


class Paddle(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.sprite_image = None
        self.x = None
        self.y = None
        self.direction = None

    def move_left(self):
        self.x+=1
        self.center_x= self.x

    def move_right(self):
        self.x-=1
        self.center_x= self.x

    def move_up(self):
        self.y+=1
        self.center_y= self.y

    def move_down(self):
        self.y-=1
        self.center_y= self.y

    
