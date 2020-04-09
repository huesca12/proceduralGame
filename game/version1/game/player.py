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

        if symbol == key.M:
            print(self.PhysicalObject.min_x)

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
