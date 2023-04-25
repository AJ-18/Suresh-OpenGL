from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def drawBone(size):
    glPushMatrix()
    glScalef(size,size,size)
    glBegin(GL_LINE_LOOP)
    glVertex3f(0,0,0)
    glVertex3f(0.1,0.1,0)
    glVertex3f(1,0,0)
    glVertex3f(0.1,-0.1,0)
    glEnd()
    glPopMatrix()