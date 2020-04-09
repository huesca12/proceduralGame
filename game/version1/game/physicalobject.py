#since visual objects are all sprites basic motion class will be a subclass of
#pyglet.sprite.Sprite
import pyglet

#make class subclass
class PhysicalObject(pyglet.sprite.Sprite):

    #initialize class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #add the velocity attributes in initialization
        self.velocity_x, self.velocity_y = 0.0, 0.0

    #update every frame; dt is a value used to account for lag in drawing
    #dt comes from the __main__ function in procedural.py (schedule_interval)
    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        
