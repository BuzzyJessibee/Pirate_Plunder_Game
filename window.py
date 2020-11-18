import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Pirate Plunder"
CHARACTER_SCALING = 1
PLAYER_MOVEMENT_SPEED = 5
TILE_SCALING = 0.5

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_list = None
        self.player_sprite = None
        self.physics_engine = None
        self.wall_list = None
        p1 = Player()

        arcade.set_background_color(arcade.csscolor.BLUE_VIOLET)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        
        # Set up the player, specifically placing it at these coordinates.
        wall_source = "Images\wall.png"

        p1.setup()
        self.player_list.append(p1.player_sprite)

        #Floor
        for x in range(0, 1250, 32):
            wall = arcade.Sprite("Images\wall.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 15
            self.wall_list.append(wall)
        
        #Ceiling
        for x in range(0, 1250, 32):
            wall = arcade.Sprite("Images\wall.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 635
            self.wall_list.append(wall)

        for y in range(0, 1250, 32):
            wall = arcade.Sprite("Images\wall.png", TILE_SCALING)
            wall.center_x = 15
            wall.center_y = y
            self.wall_list.append(wall)
            
        for y in range(0, 1250, 32):
            wall = arcade.Sprite("Images\wall.png", TILE_SCALING)
            wall.center_x = 985
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(p1.player_sprite, self.wall_list)

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        self.player_list.draw()
        self.wall_list.draw()
        # Code to draw the screen goes here

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player with the physics engine
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            p1.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            p1.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            p1.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            p1.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
    
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.W:
            p1.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            p1.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            p1.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            p1.player_sprite.change_x = 0

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

class Player:
    def __init__(self):
        self.player_sprite = None
    
    def setup(self):
        image_source = 'Images\Player.png'

        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128

if __name__ == "__main__":
    main()