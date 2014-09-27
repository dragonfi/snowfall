#!/usr/bin/python2

import sys
sys.path = ['', 'pyglet-1.1.4'] + sys.path

import math

import pyglet
from pyglet.graphics import vertex_list
from pyglet import gl
from pyglet.window import key

window = pyglet.window.Window(width=800, height=600, resizable=True)

fps_display = pyglet.clock.ClockDisplay()

num_points = 12
num_lines = 10
num_points = 12
num_lines = 12
epsilon = 0.01
lines = [[0 for i in range(num_points)] for i in range(num_lines)]
vlists = [vertex_list(num_points, 'v2f', 'c4B') for i in range(num_lines)]

for vlist in vlists:
    for i in range(len(vlist.colors)):
        vlist.colors[i] = 255

@window.event
def on_resize(w, h):
    print "on resize %d %d" % (w,h)

@window.event
def on_draw():
    window.clear()
    for vlist in vlists:
        vlist.draw(gl.GL_LINE_STRIP)
    fps_display.draw()

def update(dt):
    size = min(window.width, window.height)
    assert len(vlists) == len(lines)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] += i*j*dt*epsilon
            vlists[i].vertices[2*j] = math.cos(lines[i][j])*size/2 + size/2
            vlists[i].vertices[2*j+1] = math.sin(lines[i][j])*size/2 + size/2
            assert lines[i][0] == 0.0

@window.event
def on_key_press(sym, mod):
    pass

pyglet.clock.schedule_interval(update, 1.0/200.0)

pyglet.app.run()
