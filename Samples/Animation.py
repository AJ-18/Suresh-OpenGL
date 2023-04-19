from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pos = [0,0,0]
vel = [0.05,0.06,0.07]

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(pos[0],pos[1],pos[2])
    glutWireSphere(1,16,16)
    glPopMatrix()
    glFlush()
    glutSwapBuffers()
    for i in range(3):
        pos[i] += vel[i]
        if(pos[i] <= -4):
            vel[i] = -vel[i]
        elif(pos[i] >= 4):
            vel[i] = -vel[i]         

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 1.0, 1, 40)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,10, 0,0,0, 0,1,0)

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(500, 500)
    glutCreateWindow("A Simple Torus")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    init()
    glutMainLoop()

main()