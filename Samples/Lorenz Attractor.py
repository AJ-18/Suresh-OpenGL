import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

dt= 0.001
s=10
r=28
b=2.667

def lorenz(x,y,z):
    x_dot = x + dt*(s*(y - x))
    y_dot = y + dt*(r*x - y - x*z)
    z_dot = z + dt*(x*y - b*z)
    return x_dot, y_dot, z_dot

def display():
    n = 100000
    x,y,z = 0.0,1.0,1.05
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1)
    glBegin(GL_POINTS)
    for i in range(n):
        glVertex3f(x/50,y/50,z/50)
        x,y,z = lorenz(x,y,z)
    glEnd()
    glFlush()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(10, 10)
    glutInitWindowSize(800, 800)
    glutCreateWindow("Sample_1")
    glutDisplayFunc(display)
    glutMainLoop()

main()