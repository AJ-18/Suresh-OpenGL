import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

dt = 0.001
b = 0.208186

def thomas(x,y,z):
    x_dot = x+dt*((math.sin(y)) - b*x)
    y_dot = y + dt*((math.sin(z)) - b*y)
    z_dot = z + dt*((math.sin(x)) - b*z)
    return x_dot, y_dot, z_dot

def display():
    n = 100000
    x,y,z = 1.1, 1.1, -0.01
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1)
    glBegin(GL_POINTS)
    for i in range(n):
        glVertex3f(x/5,y/5,z/5)
        x,y,z = thomas(x,y,z)
    glEnd()
    glFlush()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(10, 10)
    glutInitWindowSize(800, 800)
    glutCreateWindow("Exercise2")
    glutDisplayFunc(display)
    glutMainLoop()

main()