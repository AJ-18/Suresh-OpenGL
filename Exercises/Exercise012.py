from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from bone import *
from math import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    








def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-12,12,-12,12,-10,10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Exercise012")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    init()
    glutMainLoop()

main()