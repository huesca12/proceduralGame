import pyglet
import math
from . import physicalobject
from pyglet.window import key



thrust = 75.0

class Player(physicalobject.PhysicalObject):

    #class constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #handler thing
        self.key_handler = key.KeyStateHandler()

        #dictionary of key states
        self.keys = dict(left=False, right=False, up=False, down=False)


    #player movement event handling
    #note that self is being passed to access the keys from the constructor
    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.DOWN:
            self.keys['down'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True

        if symbol == key.C:
            print("(" + str(self.x) + ", " + str(self.y) + ")")

        if symbol == key.D:
            print(math.sqrt((self.x-400)**2+(self.y-300)**2))

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.DOWN:
            self.keys['down'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False

        self.velocity_x = 0
        self.velocity_y = 0


    #update function for movement
    #note once again that dt and self are being accessed
    def update(self, dt):
        #run the update function on itself from procedural.py
        super(Player, self).update(dt)


        #motion handling
        if self.keys['up']:
            if self.keys['left']:
                self.velocity_x = -thrust
                self.velocity_y = thrust
            elif self.keys['right']:
                self.velocity_x = thrust
                self.velocity_y = thrust
            else:
                self.velocity_y = thrust

        if self.keys['down']:
            if self.keys['left']:
                self.velocity_x = -thrust
                self.velocity_y = -thrust
            elif self.keys['right']:
                self.velocity_x = thrust
                self.velocity_y = -thrust
            else:
                self.velocity_y = -thrust

        if self.keys['left']:
            self.velocity_x = -thrust

        if self.keys['right']:
            self.velocity_x = thrust

        #collision Handling
        #regression done in desmos
        bound1y = (0.57958*self.x)+236.315
        bound1x = (self.y-236.315)/0.57958
        bound2y = ((-0.590214)*self.x)+724.119
        bound2x = (self.y-724.119)/(-0.590214)
        bound3y = ((-0.561012)*self.x)+332.125
        bound3x = (self.y-332.125)/(-0.590214)
        bound4y = ((-0.561012)*self.x)-332.125
        bound4x = (self.y+147.852)/0.58179

        if self.y>=285:
            if self.x<=417 and self.y>=bound1y and self.x<=bound1x:
                self.velocity_x=0
                self.velocity_y=0
                self.x+=0.5
                self.y-=0.5
            if self.x>417 and self.y>=bound2y and self.x >=bound2x:
                self.velocity_x=0
                self.velocity_y=0
                self.x-=0.5
                self.y-=0.5
        if self.y<=285:
            if self.x<=417 and self.y<=bound3y and self.x<=bound3x:
                self.velocity_x=0
                self.velocity_y=0
                self.x+=0.5
                self.y+=0.5
            if self.x>417 and self.y>=bound4y and self.x >=bound4x:
                self.velocity_x=0
                self.velocity_y=0
                self.x-=0.5
                self.y+=0.5
