import pyglet
#create player object
player = pyglet.media.Player()
#turn looping on
player.loop = True

#player function
def playMusic(music):
    player.queue(music)
    player.play()

def nextMusic(music):
    player.queue(music)
    player.next_source()
