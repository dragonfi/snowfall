#!/usr/bin/python2

import pyglet

from random import randint, uniform

window = pyglet.window.Window()

pyglet.resource.path = ['.', 'data',
        '/home/dragonfi/prog/humble-bullet-curtain/data']
pyglet.resource.reindex()

fps_display = pyglet.clock.ClockDisplay()
flake_counter = pyglet.text.Label(text = '0')

snowflake = pyglet.resource.image('white-arrow.png')
snowflake.anchor_x = snowflake.width / 2
snowflake.anchor_y = snowflake.height / 2

max_snowflakes = 1000
snowflakes = []
snowflakes_batch = pyglet.graphics.Batch()

@window.event
def on_resize(w, h):
    print "on resize %d %d" % (w,h)

@window.event
def on_draw():
    window.clear()
    snowflakes_batch.draw()
    fps_display.draw()
    flake_counter.draw()

def update(dt):
    if len(snowflakes) < max_snowflakes:
        s = pyglet.sprite.Sprite(
            snowflake,
            x=randint(0, window.width),
            y=window.height,
            batch=snowflakes_batch)
        s.vx = 0
        s.vy = -1
        s.vrotation = 0
        snowflakes.append(s)
        flake_counter.text = str(len(snowflakes))

    wh = window.height
    ww = window.width

    for s in snowflakes:
        s.vy += uniform(-0.05, 0.05)
        s.vx += uniform(-0.05, 0.05)
        s.set_position((s.x + s.vx) % ww, (s.y + s.vy) % wh)
        s.vrotation += uniform(-0.05, 0.05)
        s.rotation += s.vrotation


pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()
