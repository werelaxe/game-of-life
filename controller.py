import sys

from OpenGL.GLUT import GLUT_LEFT_BUTTON, GLUT_DOWN

import open_gl


def keyboard(key, x, y):
    if key == b'\x1b':
        sys.exit(0)
    if key == b' ':
        open_gl.run = 1 - open_gl.run
    if key == b'c':
        open_gl.field.clear()
    if key == b'r':
        open_gl.field.randomizate()
    print('keyboard:', key, x, y)


def keyboard_up(key, x, y):
    print('keyboard up:', key, x, y)


def keyboard_func(key, x, y):
    print('keyboard func:', key, x, y)


def keyboard_up_func(key, x, y):
    print('keyboard up func:', key, x, y)


def mouse(button, state, x, y):
    print('mouse:', button, state, x, y)
    #if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
    #    open_gl.field.change((x // open_gl.draw_size, y // open_gl.draw_size))
