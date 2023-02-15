import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

#draw one curve, then use the function 3 times to get the full snowflake
#drawline, rotate, drawline rotate, etc...
#divide line by 3 (3 segments).  


def display():
    s = int(input("Enter s value: "))
    n = int(input("Enter n value: "))

    N = 3 * (4**n)
    threeP = 3**n
    S = (s / (threeP))
    Perimeter = N * S


    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1)
    glBegin(GL_LINE_LOOP)
    for i in range(n-1):
        glVertex2f(x,y)
    glEnd()
    glFlush()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(10, 10)
    glutInitWindowSize(800, 800)
    glutCreateWindow("Exercise3")
    glutDisplayFunc(display)
    glutMainLoop()

main()