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

    #prevent object from flying off screen
    def check_bounds(self):
        min_x = -self.image.width/2
        min_y = -self.image.height/2
        max_x = 800 + self.image.width/2
        max_y = 600 + self.image.width/2
        if self.x < min_x:
            self.x = min_x
        elif self.x > max_x:
            self.x = max_x
        elif self.y < min_y:
            self.y = min_y
        elif self.y > max_y:
            self.y = max_y
