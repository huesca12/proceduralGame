from . import physicalobject

thrust = 150.0

class Player(physicalobject.PhysicalObject):

    #class constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.DOWN:
            self.keys['down'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False

    #update function for movement
    #note once again that dt and self are being accessed
    def update(self, dt):
        #run the update function on itself from procedural.py
        super(Player, self).update(dt)

        print(self.keys)

        #motion handling
        #if self.keys['up']:
        #    if self.keys[]
