from OpenGL.GL import glBegin, GL_QUADS, glColor3f,\
    glVertex3f, glEnd, glLineWidth, GL_LINE_STRIP, GL_LINES, glRectf


def draw_cube(x1, y1, z1, x2, y2, z2):
    glBegin(GL_QUADS)

    glColor3f(0, 0, 1)
    glVertex3f(x1, y1, z1)
    glVertex3f(x2, y1, z1)
    glVertex3f(x2, y2, z1)
    glVertex3f(x1, y2, z1)

    glColor3f(0, 1, 0)
    glVertex3f(x1, y1, z2)
    glVertex3f(x2, y1, z2)
    glVertex3f(x2, y2, z2)
    glVertex3f(x1, y2, z2)

    glColor3f(0, 1, 1)
    glVertex3f(x1, y1, z1)
    glVertex3f(x2, y1, z1)
    glVertex3f(x2, y1, z2)
    glVertex3f(x1, y1, z2)

    glColor3f(1, 0, 0)
    glVertex3f(x1, y2, z1)
    glVertex3f(x2, y2, z1)
    glVertex3f(x2, y2, z2)
    glVertex3f(x1, y2, z2)

    glColor3f(1, 0, 1)
    glVertex3f(x1, y1, z1)
    glVertex3f(x1, y1, z2)
    glVertex3f(x1, y2, z2)
    glVertex3f(x1, y2, z1)

    glColor3f(1, 1, 0)
    glVertex3f(x2, y1, z1)
    glVertex3f(x2, y1, z2)
    glVertex3f(x2, y2, z2)
    glVertex3f(x2, y2, z1)

    glEnd()


def draw_net(x1, y1, z1, x2, y2, z2):
    glLineWidth(2)
    glBegin(GL_LINE_STRIP)
    glVertex3f(x1, y1, z1)
    glVertex3f(x2, y1, z1)
    glVertex3f(x2, y2, z1)
    glVertex3f(x1, y2, z1)
    glVertex3f(x1, y1, z1)
    glVertex3f(x1, y1, z2)
    glVertex3f(x2, y1, z2)
    glVertex3f(x2, y2, z2)
    glVertex3f(x1, y2, z2)
    glVertex3f(x1, y1, z2)
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(x1, y2, z2)
    glVertex3f(x1, y2, z1)

    glVertex3f(x2, y2, z2)
    glVertex3f(x2, y2, z1)

    glVertex3f(x2, y1, z2)
    glVertex3f(x2, y1, z1)
    glEnd()


def draw_field(field):

    if field.dim == 2:
        if field.heat_map:
            for cell in field.heat_cells:
                if cell in field.active_cells:
                    glColor3f(field.heat_cells[cell], 1, 0)
                else:
                    glColor3f(field.heat_cells[cell], 0, 0)
                glRectf(cell[1], cell[0], cell[1] + 1, cell[0] + 1)
        else:
            for cell in field.active_cells:
                glColor3f(0, 1, 0)
                glRectf(cell[1], cell[0], cell[1] + 1, cell[0] + 1)

    else:
        if field.dim == 3:
            for top, left, depth in field.active_cells:
                draw_cube(left, top, depth, left + 1, top + 1, depth + 1)
        else:
            raise NotImplementedError

