#Arjun Suresh (AJ)
#Project 05


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

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

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    # Convert elapsed time to frame number
    f = int(30*glutGet(GLUT_ELAPSED_TIME) / 1000) / 180
    # Determine angle of rotation based on frame number
    r = (sin(f*pi)*4)
    # Start 1
    glPushMatrix()
    glTranslatef(0,0,0)
    glRotatef(r,0,0,1)
    glColor3f(0, 1, 0) # set color to green
    drawBone(2)
    # Start 2
    glPushMatrix()
    glTranslatef(2,0,0)
    glRotatef(r,0,0,1)
    drawBone(2)
    # Start 3
    glPushMatrix()
    glTranslatef(2,0,0)
    glRotatef(r,0,0,1)
    drawBone(2) 
    # Start 4
    glPushMatrix()
    glTranslatef(2,0,0)
    glRotatef(r,0,0,1)
    drawBone(2) 
    # Start 5
    glPushMatrix()
    glTranslatef(2,0,0)
    glRotatef(r,0,0,1)
    drawBone(2) 
    # End 1   
    glPopMatrix() 
    # End 2   
    glPopMatrix() 
    # End 3   
    glPopMatrix()
    # End 4
    glPopMatrix()
    # End 5
    glPopMatrix()
    glFlush()
    glutSwapBuffers()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-12,12,-12,12,-10,10)
    gluLookAt(-1, 0, 0, 1, 0, -3, 0, 0, -1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Project 5 AJ")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    init()
    glutMainLoop()

main()