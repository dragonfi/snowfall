#!/usr/bin/python2

import pyglet

window = pyglet.window.Window()

pyglet.resource.path = ['data']
pyglet.resource.reindex()

arrow = pyglet.resource.image('white-arrow.png')
bullet = pyglet.sprite.Sprite(arrow)


@window.event
def on_resize(w, h):
    print "on resize %d %d" % (w,h)

@window.event
def on_draw():
    window.clear()
    bullet.draw()

def update(dt):
    bullet.x += 3
    bullet.y += 2
    bullet.x %= window.width
    bullet.y %= window.height
    bullet.rotation += 1

pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()
