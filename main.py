#!/usr/bin/python2

import pyglet

from random import random, randint

window = pyglet.window.Window()

pyglet.resource.path = ['data']
pyglet.resource.reindex()

fps_display = pyglet.clock.ClockDisplay()
flake_counter = pyglet.text.Label(text = '0')

snowflake = pyglet.resource.image('white-arrow.png')
snowflake.anchor_x = snowflake.width / 2
snowflake.anchor_y = snowflake.height / 2

max_snowflakes = 1000
snowflakes = []

@window.event
def on_resize(w, h):
    print "on resize %d %d" % (w,h)

@window.event
def on_draw():
    window.clear()
    for s in snowflakes:
        s.draw()
    fps_display.draw()
    flake_counter.draw()

def update(dt):
    if len(snowflakes) < max_snowflakes:
        s = pyglet.sprite.Sprite(
            snowflake,
            x=randint(0, window.width),
            y=window.height)
        s.vx = 0
        s.vy = -1
        s.vrotation = 0
        snowflakes.append(s)
        flake_counter.text = str(len(snowflakes))

    for s in snowflakes:
        s.vx += (random() - 0.5) / 10.0
        s.vy += (random() - 0.5) / 10.0
        s.vrotation += (random() - 0.5) / 2.0

        s.x += s.vx
        s.y += s.vy
        s.rotation += s.vrotation
        s.x %= window.width
        s.y %= window.height


pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()
