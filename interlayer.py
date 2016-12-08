from OpenGL.GLUT import GLUT_SCREEN_WIDTH, glutGet, GLUT_SCREEN_HEIGHT

from field import Field


def get_resolution():
    screen_width = glutGet(GLUT_SCREEN_WIDTH)
    screen_height = glutGet(GLUT_SCREEN_HEIGHT)
    return screen_width, screen_height


def get_params(field):
    dim = field.dim
    if not ((dim == 1) or (dim == 2) or (dim == 3)):
        raise NotImplementedError
    width = field.size
    height = field.size
    if dim == 1:
        height = 1
    ws, hs = get_resolution()
    draw_size = min(ws / width, (hs - 90) / height)
    return dim, width, height, draw_size
