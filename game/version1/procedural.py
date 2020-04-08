import pyglet
from pyglet.window import key
from game import people
from game import physicalobject
from game import music
from game import player
#make game window
game_window = pyglet.window.Window(800,600)
#define where to find resources
pyglet.resource.path = ['../resources'] #it is a list of sources I imagine
#reindex where the resouces are (rediscover as it were)
pyglet.resource.reindex()

#create main main_batch to add graphics to
main_batch = pyglet.graphics.Batch()

#create a resource object from corresponding image
ground = pyglet.resource.image("groundProcedural.png")
testplayer = pyglet.resource.image("test-player.png")
person = pyglet.resource.image("test-person.png")

#grab music
theme = pyglet.resource.media("death.wav")

#grab effect sounds
boom = pyglet.resource.media("8bit_bomb_explosion.wav")

#start music
music.playMusic(theme)

#a function to anchor images at their center as to be able to rotate them
#not terribly relevant to our purposes
def center_image(image):
    image.anchor_x = image.width//2
    image.anchor_y = image.height//2

#center player
center_image(testplayer)

#player should be instance of Sprite subclass --> make player PhysicalObject
#which is child of Sprite to access motion styff
#physicalobject.PhysicalObject(etc.) --> make player Player object
#which is child of PhysicalObject to access player control
player = player.Player(img=testplayer, x=400, y=300,
                                       batch=main_batch)
floor = pyglet.sprite.Sprite(img=ground, x=0, y=0, batch=main_batch)
peopleList = people.spawn(4,person,main_batch)

#make player into list of itself to concatenate into game_objects module; they
#must all be an instance of or child of PhysicalObject
game_objects = peopleList + [player]

#get some labels going; add to main batch
score_label = pyglet.text.Label(text="Casualties: 0", x=10, y=460)
game_label = pyglet.text.Label(text="Politically Inappropriate Pre-Release",
                                x=game_window.width//2,y=game_window.height//2,
                                anchor_x='center')
                                #centered with anchor_x

################
#Update Handling
################

#function iterating over list of game_objects
def update(dt):
    for obj in game_objects:
        obj.update(dt)

###############
#Event Handling
###############

#redraws when appropriate; the @game_window.event decorator lets the Window
#know the following is an event handler
@game_window.event
def on_draw():
    #clear screen first!
    game_window.clear()

    #draw main_batch
    main_batch.draw()
    #draw text
    score_label.draw()
    game_label.draw()

#key press event manager
@game_window.event
def on_key_press(symbol, modifiers):
    if symbol == key.B:
        print("boom")
        boom.play()
        # TODO: fix weird error thrown when you spam B; prob with some sort of timeout

#makes sure event loop is only entered if this is the executed file
if __name__ == '__main__':
    #for smooth animation we need a refresh rate of 120hz (times per second)
    #double the most common 60hz refresh rotate
    #define
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
