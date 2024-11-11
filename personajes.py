import arcade
from helper import *

class Toad(arcade.Sprite):
    DIRECCION_DERECHA = 0
    DIRECCION_IZQUIERDA = 1
    ESTADO_COLGADO = 0

    def load_texture_pair(self, filename):
        """
        Load a texture pair, with the second being a mirror image.
        """
        return [
            arcade.load_texture(filename),
            arcade.load_texture(filename, flipped_horizontally=True),
        ]


    def __init__(self):
        super().__init__()
        self.texture_colgado = [None]*2
        self.texture_colgado[0] = self.load_texture_pair("sprites/toads/colgado-001.png")
        self.texture_colgado[1] = self.load_texture_pair("sprites/toads/colgado-002.png")
        self.indice = 0
        self.estado = self.ESTADO_COLGADO
        self.direcion = self.DIRECCION_DERECHA
        self.texture = self.texture_colgado[self.indice][self.direcion]
        self.delta_acumulado = 0
        self.cuadros_por_segundo = 1/3
        self.incremento_cuadro_1 = 148
        self.incremento_cuadro_2 = 148

        joysticks = arcade.get_joysticks()
        print(joysticks)
        # If we have any...
        if joysticks:
            # Grab the first one in  the list
            self.joystick = joysticks[2]

            # Open it for input
            self.joystick.open()

            # Push this object as a handler for joystick events.
            # Required for the on_joy* events to be called.
            self.joystick.push_handlers(self)
        else:
            # Handle if there are no joysticks.
            print("There are no joysticks, plug in a joystick and run again.")
            self.joystick = None

        self.posicion_mano_derecha = (0,0)
        self.posicion_mano_izquierda = (0, 0)
        self.posicion_talon_derecho = (0, 0)
        self.posicion_talon_izquierdo = (0, 0)



    def on_update(self, delta_time: float = 1 / 60):
        """ Move the player """
        # If there is a joystick, grab the speed.
        if self.joystick:

            # x-axis
            # print("X:{} y:{}".format(self.joystick.x, self.joystick.y))
            self.change_x = self.joystick.x * MOVEMENT_SPEED
            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                self.change_x = 0

            # y-axis
            # if self.change_x!=0:

            self.change_y = -self.joystick.y * MOVEMENT_SPEED
            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.change_y = 0

        # Move the player
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Keep from moving off-screen
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

        if self.change_x > 0:
            self.direcion = self.DIRECCION_DERECHA
        elif self.change_x < 0:
            self.direcion = self.DIRECCION_IZQUIERDA

        self.delta_acumulado += delta_time
        if self.delta_acumulado>self.cuadros_por_segundo:
            self.indice= (self.indice+1)%2
            self.delta_acumulado = 0
        self.texture = self.texture_colgado[self.indice][self.direcion]
        self.hit_box = self.texture.hit_box_points
        if self.direcion == self.DIRECCION_DERECHA:
            if self.indice == 0:
                self.posicion_mano_derecha = (self.left + 85, self.top-10)
                self.posicion_talon_derecho = (self.left + 62, self.top - 117)
                self.posicion_mano_izquierda = (self.left + 104, self.top - 101)
            if self.indice == 1:
                self.posicion_mano_derecha = (self.left + 67, self.top-10)
                self.posicion_talon_derecho = (self.left + 62, self.top - 117)
                self.posicion_mano_izquierda = (self.left + 104, self.top - 101)
        if self.direcion == self.DIRECCION_IZQUIERDA:
            if self.indice == 0:
                self.posicion_mano_derecha = (self.left+53, self.top)
                self.posicion_talon_derecho = (self.left + 62, self.top - 117)
                self.posicion_mano_izquierda = (self.left + 104, self.top - 101)
            if self.indice == 1:
                self.posicion_mano_derecha = (self.left+60, self.top)
                self.posicion_talon_derecho = (self.left + 50, self.top - 148)

                self.posicion_mano_izquierda = (self.left + 82, self.top - 123)

        print("center x: {}\ncenter y: {}\nwith: {}\nheight: {}\ntalon derecho pos x: {}\ntalon derecho pos y: {}\n".format(self.center_x, self.center_y, self.width, self.height, self.posicion_talon_derecho[0], self.posicion_talon_derecho[1]))