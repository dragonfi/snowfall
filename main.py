#!/usr/bin/python2


import sys
sys.path = ['', 'pyglet-1.1.4'] + sys.path

import pyglet
from pyglet.window import key

from random import randint, uniform, choice

window = pyglet.window.Window(width=800, height=600, resizable=True)

pyglet.resource.path = ['.', 'data', '/home/dragonfi/python/snowfall/data']
pyglet.resource.reindex()

def add_snowflake_image(images, name):
    snowflake = pyglet.resource.image(name)
    snowflake.anchor_x = snowflake.width / 2
    snowflake.anchor_y = snowflake.height / 2
    images.append(snowflake)

def add_circle_image(images, r=50):
    img = pyglet.image.create(r*2, r*2)
    data = ["\xff\xff\xff\xff" if i*i+j*j < r*r else "\x00\x00\x00\x00" for i in range(-r, r) for j in range(-r, r)]
    flat_data = "".join(data)
    img.set_data('RGBA', r*2*4, flat_data)
    img.anchor_x = img.width / 2
    img.anchor_y = img.height / 2
    images.append(img)

snowflake_images = []

for name in ('snowflake-filled.png', 'snowflake-frame.png', 'snowflake.png'):
    add_snowflake_image(snowflake_images, name)

add_circle_image(snowflake_images)

max_snowflakes = 1000
max_a = max_acceleration = 2.0
max_rot_a = max_rot_acceleration = 1.0
target_fps = 20.0
flake_size = 0.2
rotation_enabled = True

snowflakes = []
snowflakes_batch = pyglet.graphics.Batch()

transparent_grey_color = (128, 128, 128, 128)
font_size = 20

target_fps_label_x_offset = -10
flake_size_label_x_offset = -90
flake_counter_label_x_offset = -170

target_fps_label = pyglet.text.Label(text = str(target_fps),
        x = window.width + target_fps_label_x_offset,
        y = 10,
        color = transparent_grey_color,
        font_size = 20,
        anchor_x = 'right')

flake_size_label = pyglet.text.Label(text = str(flake_size),
        x = window.width + flake_size_label_x_offset,
        y = 10,
        color = transparent_grey_color,
        font_size = 20,
        anchor_x = 'right')

flake_counter_label = pyglet.text.Label(text = str(len(snowflakes)),
        x = window.width + flake_counter_label_x_offset,
        y = 10,
        color = transparent_grey_color,
        font_size = 20,
        anchor_x = 'right')

fps_display = pyglet.clock.ClockDisplay()
@window.event
def on_resize(w, h):
    print "on resize %d %d" % (w,h)
    target_fps_label.x = window.width + target_fps_label_x_offset
    flake_size_label.x = window.width + flake_size_label_x_offset
    flake_counter_label.x = window.width + flake_counter_label_x_offset

@window.event
def on_draw():
    window.clear()
    snowflakes_batch.draw()
    fps_display.draw()
    flake_counter_label.draw()
    target_fps_label.draw()
    flake_size_label.draw()

def update(dt):
    if pyglet.clock.get_fps() >= target_fps * 0.95:
        s = pyglet.sprite.Sprite(
            choice(snowflake_images),
            x=randint(0, window.width),
            y=window.height,
            batch=snowflakes_batch)
        s.scale = uniform(0.05, flake_size)
        s.vx = 0.0
        s.vy = -0.5
        s.vrotation = 0
        s.y = window.height + s.height // 2
        snowflakes.append(s)
        flake_counter_label.text = str(len(snowflakes))

    wh = window.height
    ww = window.width

    for s in snowflakes:
        if s.vy > 0.0:
            s.vy += uniform(-max_a / 10.0, 0.00)
        s.vy += uniform(-max_a, max_a)
        s.vx += uniform(-max_a, max_a)
        s.set_position((s.x + s.vx * dt), (s.y + s.vy * dt))
        if out_of_bounds(s):
            snowflakes.remove(s)
        if rotation_enabled:
            s.vrotation += uniform(-max_rot_a, max_rot_a)
            s.rotation += s.vrotation * dt

def out_of_bounds(s):
    ww = window.width
    wh = window.height
    return (s.x < -s.width or s.x > ww + s.width
        or s.y < -s.height or s.y > wh + s.height)

@window.event
def on_key_press(sym, mod):
    global target_fps
    global flake_size
    global rotation_enabled
    if sym == key.W or sym == key.NUM_ADD:
        target_fps += 1.0
    if sym == key.S or sym == key.NUM_SUBTRACT:
        target_fps -= 1.0
    if sym == key.E or sym == key.NUM_MULTIPLY:
        flake_size += 0.05
    if (sym == key.D or sym == key.NUM_DIVIDE) and flake_size >= 0.1:
        flake_size -= 0.05
    if sym == key.NUM_0:
        rotation_enabled = not rotation_enabled

    target_fps_label.text = str(target_fps)
    flake_size_label.text = str(flake_size)

pyglet.clock.schedule_interval(update, 1.0/200.0)

pyglet.app.run()
