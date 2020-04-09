import pyglet

def startMenu(menu, window):

    def on_draw():
        window.clear()
        menu.draw()
    window.push_handlers(on_draw)
