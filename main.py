    """ Sprite Sample Program """

import arcade

from personajes import *
from helper import *
# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5


MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "redibujados With Walls Example")
        self.lista_toads = arcade.SpriteList()
        self.lista_toads.append(Toad())
        self.lista_toads[0].center_y = 300
        self.lista_toads[0].center_x = 400



    def setup(self):
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_line (SCREEN_WIDTH / 2, SCREEN_HEIGHT, self.lista_toads[0].posicion_mano_derecha[0], self.lista_toads[0].posicion_mano_derecha[1], arcade.color.RED)
        self.lista_toads.draw()
        arcade.draw_line(self.lista_toads[0].posicion_mano_derecha[0], self.lista_toads[0].posicion_mano_derecha[1], self.lista_toads[0].posicion_talon_derecho[0],
                         self.lista_toads[0].posicion_talon_derecho[1], arcade.color.RED)
        arcade.draw_line(self.lista_toads[0].posicion_talon_derecho[0], self.lista_toads[0].posicion_talon_derecho[1], self.lista_toads[0].posicion_mano_izquierda[0],
                         self.lista_toads[0].posicion_mano_izquierda[1], arcade.color.RED)
        arcade.draw_circle_filled(self.lista_toads[0].center_x,
                         self.lista_toads[0].center_y,10, arcade.color.RED)

    def on_update(self, delta_time: float):
        self.lista_toads.on_update(delta_time)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.O:
            self.lista_toads[0].talon_derecho=(self.lista_toads[0].talon_derecho[0], self.lista_toads[0].talon_derecho[1]-1)

        elif key == arcade.key.P:
            self.lista_toads[0].talon_derecho=(self.lista_toads[0].talon_derecho[0], self.lista_toads[0].talon_derecho[1]+1)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()