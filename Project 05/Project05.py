from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from bone import *
from math import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    # Convert elapsed time to frame number
    f = int(30*glutGet(GLUT_ELAPSED_TIME) / 1000) / 30
    # Determine angle of rotation based on frame number
    r = abs(sin(f*pi)*45)
    # Start 1
    glPushMatrix()
    glTranslatef(0,0,0)
    glRotatef(r,0,0,1)
    drawBone(4)
    # Start 2
    glPushMatrix()
    glTranslatef(4,0,0)
    glRotatef(r,0,0,1)
    drawBone(4)
    # Start 3
    glPushMatrix()
    glTranslatef(4,0,0)
    glRotatef(r,0,0,1)
    drawBone(2) 
    # End 1   
    glPopMatrix() 
    # End 2   
    glPopMatrix() 
    # End 3   
    glPopMatrix()
    glFlush()
    glutSwapBuffers()

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
    glutCreateWindow("Articluated Figure")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    init()
    glutMainLoop()

main()