import sys
from field import Field
from controller import keyboard, keyboard_func, mouse, keyboard_up
from draw import draw_field
from multiprocessing import Process, Pipe
from argparse import ArgumentParser
from interlayer import get_params, get_resolution
from OpenGL.GL import GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT,\
    glClear, glTranslatef, glRotatef, glEnable, \
    GL_DEPTH_TEST, glMatrixMode, GL_PROJECTION,\
    glLoadIdentity, glOrtho, GL_MODELVIEW, GL_TRUE, glRectf, glColor3f
from OpenGL.raw.GLU import gluOrtho2D
from OpenGL.GLUT import glutSwapBuffers, glutGet,\
    GLUT_ELAPSED_TIME, glutTimerFunc, glutInitDisplayMode, \
    glutInitWindowSize, glutInitWindowPosition, glutInit,\
    glutCreateWindow, glutDisplayFunc, GLUT_DOUBLE, GLUT_RGB, \
    glutKeyboardFunc, glutKeyboardUpFunc, glutSpecialFunc,\
    glutIgnoreKeyRepeat, glutMouseFunc, glutMainLoop, glutPostRedisplay, GLUT_SCREEN_WIDTH, GLUT_SCREEN_HEIGHT

t = 0

def draw():
    global field
    draw_field(field)
    # drawing


def timer(value=0):
    global field
    field.update()
    # here was timer, but it was shit
    glutPostRedisplay()
    glutTimerFunc(delay, timer, delay)


def display():
    global dim_count
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if dim_count == 3:
        glLoadIdentity()
        glRotatef(-45, 0, 1, 0)
        glRotatef(25, 1, 0, -1)
        glTranslatef(0, -2, 0)
    draw()
    glutSwapBuffers()


def variables_init():
    global win_size_x
    global win_size_y
    global dim_count
    global width
    global height
    global delay
    global draw_size
    global field
    delay = 1000
    field = Field(3, 10, (2, 3), heat_map=True)

    # field.active_cells = {(3, 0, 0): 1, (3, 1, 0): 1, (3, 2, 0): 1}
    params = get_params(field)
    dim_count, width, height, draw_size = params
    win_size_x = int(width * draw_size)
    win_size_y = int(height * draw_size)


def opengl_init():
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(win_size_x, win_size_y)
    sc_width, sc_height = get_resolution()
    glutInitWindowPosition(sc_width // 2 - win_size_x // 2,
                           sc_height // 2 - win_size_y // 2)
    # glutInit()
    glutCreateWindow(b'Game of life')
    glutDisplayFunc(display)

    if dim_count == 3:
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-width / 2, width / 2, -height / 2, height / 2, -200, 200)
        glMatrixMode(GL_MODELVIEW)
        glRotatef(-45, 0, 1, 0)
        glRotatef(25, 1, 0, -1)
        glTranslatef(0, -2, 0)

    else:
        gluOrtho2D(0, width, height, 0)

    glutTimerFunc(delay, timer, 0)
    glutKeyboardFunc(keyboard)
    glutKeyboardUpFunc(keyboard_up)
    glutSpecialFunc(keyboard_func)
    glutIgnoreKeyRepeat(GL_TRUE)
    glutMouseFunc(mouse)


def run_main_loop():
    glutMainLoop()
