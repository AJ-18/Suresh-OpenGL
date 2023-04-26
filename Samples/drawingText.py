from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    text = "Hello World!"
    glColor3f(1,0,0)
    glRasterPos2f(0,0)    
    for c in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 200)
glutCreateWindow("Drawing Text")
glutDisplayFunc(display)
glutMainLoop()