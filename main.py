#!/usr/bin/python2

import pyglet

from random import random, randint

window = pyglet.window.Window()

pyglet.resource.path = ['data']
pyglet.resource.reindex()

arrow = pyglet.resource.image('white-arrow.png')
snowflake = pyglet.resource.image('white-arrow.png')

bullet = pyglet.sprite.Sprite(arrow)

max_snowflakes = 1000
snowflakes = []

@window.event
def on_resize(w, h):
    print "on resize %d %d" % (w,h)

@window.event
def on_draw():
    window.clear()
    bullet.draw()
    for s in snowflakes:
        s.draw()

def update(dt):
    if len(snowflakes) < max_snowflakes:
        snowflakes.append(pyglet.sprite.Sprite(
            snowflake,
            x=randint(0, window.width),
            y=randint(0, window.height)))

    for s in snowflakes:
        s.x += random() - 0.5
        s.y -= random()
        s.x %= window.width
        s.y %= window.height
        s.rotation += random() - 0.5

    bullet.x += 3
    bullet.y += 2
    bullet.x %= window.width
    bullet.y %= window.height
    bullet.rotation += 1

pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()
