import pyglet
import random
from . import physicalobject

#person maker
def spawn(number, image, batch):
    #list of new person objects as sprites
    people = []
    #make desired number
    for i in range(number):
        #random spawns in center rectangle
        person_x = random.randint(100,700)
        person_y = random.randint(200,400)
        #create new person sprite of subclass PhysicalObject
        new_person = physicalobject.PhysicalObject(img=image,x=person_x,
                                          y=person_y,
                                          batch=batch)

        #append to list
        people.append(new_person)
    #return new people
    return people
