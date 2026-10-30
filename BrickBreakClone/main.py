"""
Clone of Brick Break - Version 1.0

A game where a ball strikes blocks after being bounced off a paddle.
"""

import arcade


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Brick Break Clone"
blinder = 300
blinder2 = 900
arcade.enable_timings()
BRICK_COUNT = 10


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.AMAZON
        self.player_sprite = None
        self.ball_sprite = None
        self.player_list = None
        self.ball_list = None
        self.brick_list= None
        self.ball_initial = True
        self.binding = None
        self.binding2= None
        self.brick_sprite=None

        self.score_text = None
        self.level_text = None
        self.lives_text = None
        self.ball_y = 0
        self.ball_x = 0
        self.bounce = 1
        self.score = 0
        self.bricks = 0
        self.Balls = None
        self.Level = 1
        self.lives = 0
        

        # If you have sprite lists, you should create them here,
        # and set them to None
    def setup(self):
        self.score_text = arcade.Text("Score:",1000,300,[255,255,255])
        self.level_text = arcade.Text("Level: 1",1000,250,[255,255,255])
        self.lives_text = arcade.Text("Lives: 0",1000,200,[255,255,255])
        
        self.player_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.brick_list = arcade.SpriteList()

        self.binding = arcade.shape_list.create_rectangle_filled(600,WINDOW_HEIGHT/2,600,WINDOW_HEIGHT,[100,0,100,255],0)
        
        self.player_sprite = arcade.Sprite("editingfiles/paddle5.png", scale = 1)
        self.player_sprite.position = WINDOW_WIDTH/2, WINDOW_HEIGHT/12

        self.ball_sprite = arcade.Sprite("editingfiles/Ball.png", scale = 1)
        
        #self.ball_sprite.position = WINDOW_WIDTH/2, WINDOW_HEIGHT/2
        
        self.player_list.append(self.player_sprite)
        self.ball_list.append(self.ball_sprite)

        self.LevelMove()

        #self.binding = arcade.shape_list.create_rectangle_filled(blinder/2,WINDOW_HEIGHT/2,blinder,WINDOW_HEIGHT,[0,0,0,0],0)
        #self.binding2 = arcade.shape_list.create_rectangle_filled(1090,WINDOW_HEIGHT/2,380,WINDOW_HEIGHT,[0,0,0,0],0)
        

        self.ball_y = 2
        self.ball_x = 2

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
        self.binding.draw()
        self.score_text.draw()
        self.level_text.draw()
        self.lives_text.draw()
        #self.binding2.draw()
        self.brick_list.draw()
        self.player_list.draw()
        self.ball_list.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.score_text.text = f"Score: {self.score}"
        self.level_text.text = f"Level: {self.Level}"
        self.lives_text.text = f"lives: {self.lives}"

        
        brick_hit = arcade.check_for_collision_with_list(self.ball_sprite,self.brick_list)
        
        if self.ball_sprite.center_x >= blinder2: #or self.ball_sprite.center_x <= blinder:
            if self.ball_x > 0:
                self.ball_x = -self.ball_x
                self.BounceCalc(0.5)
            print("Brocoli")
        if self.ball_sprite.center_x <= blinder:
            if self.ball_x < 0:
                self.ball_x = -self.ball_x
                self.BounceCalc(0.5)
            print("Brocoli Plus")
            
        if self.ball_sprite.center_y >= WINDOW_HEIGHT:
            self.ball_y = -self.ball_y
            self.BounceCalc(0.5)
            print("fiber")

        if arcade.check_for_collision(self.player_sprite,self.ball_sprite):
            self.CollisionEvents(1)

        for brick in brick_hit:
            
            self.CollisionBrick(brick)

            brick.remove_from_sprite_lists()
            self.bricks -=1
            if self.ball_x > 0:
                self.ball_x = 2
            else:
                self.ball_x = -2

            if self.bricks == 0:
                self.Level+=1
                self.LevelMove()
        #print(self.brick_list)

        if self.ball_sprite.center_y <= 0:
            self.ball_initial = True
            self.ball_sprite.position = self.player_sprite.center_x, self.player_sprite.center_y+30
            self.lives+=1
            print("death")
            
        if not self.ball_initial:
            self.ball_sprite.center_y+=(self.ball_y*self.bounce)
            self.ball_sprite.center_x+=(self.ball_x*self.bounce)
            print(arcade.get_fps())
        else:
            self.ball_x = 0
            self.ball_y = 3
            self.bounce = 1
            #print("Crack")

        


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        Space = 32

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        #print(key)
        #if key == 32:
         #   while PauseCheck:
         #       continue
            

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        
        if not(x < blinder+80 or x > blinder2-80) :
            self.player_sprite.center_x = x
            if self.ball_initial:
                self.ball_sprite.position = x,self.player_sprite.center_y+30

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.ball_initial = False

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def CollisionEvents(self,number):
        if self.ball_y < 0:
            self.ball_y = -self.ball_y
            self.score+=100
        
        if self.ball_sprite.center_x > self.player_sprite.center_x+20:
            self.ball_x = 1
        elif self.ball_sprite.center_x < self.player_sprite.center_x-20:
            self.ball_x = -1
        elif self.ball_sprite.center_x > self.player_sprite.center_x+10:
            self.ball_x = 0.5
        elif self.ball_sprite.center_x < self.player_sprite.center_x-10:
            self.ball_x = -0.5
        else:
            self.ball_x = 0
        
        print(f"Bounce: {self.bounce}")
        print(f"Score: {self.score}")
        print(f"Center_x: {(self.player_sprite.center_x+10) < self.ball_sprite.center_x }")

    def CollisionBrick(self,brick):
        #self.ball_y = -self.ball_y
        if self.ball_sprite.center_x <= brick.center_x-30:
            self.ball_x = -self.ball_x
        elif self.ball_sprite.center_x >= brick.center_x+30:
            self.ball_x = -self.ball_x
        else:
            self.ball_y = -self.ball_y
        self.score+=1000
        print(f"Bounce: {self.bounce}")
        print(f"Score: {self.score}")

    def BounceCalc(self, calculation):
        if self.bounce < 2:
            self.bounce+=calculation
        else:
            self.bounce+=0.01


    def LevelMove(self):
        tick = 0
        ticky = 0

        for i in range(BRICK_COUNT * self.Level):
            brick_sprite = arcade.Sprite("editingfiles/Brick.png",scale = 1)
            self.bricks+=1
            
            if i%10 == 0 and i!=0:
                ticky+=1
                tick = 0
                print(i)
            elif i!=0:
                tick+=1
            brick_sprite.center_x = 330 + (tick * 60)
            brick_sprite.center_y = 500 - (ticky *15)
            self.brick_list.append(brick_sprite)
            


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()
    game.setup()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()



if __name__ == "__main__":
    main()
