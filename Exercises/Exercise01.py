import OpenGL
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    x = 0
    y = 1
    n = int (input("Enter number of points: "))

    #RADIANS
    step = 6.28319/n
    #DEGREES
    step2 = 360.0/n

    #OPENGL wants degrees, python wants radians

    glBegin(GL_LINE_LOOP)
    glVertex2f(x, y)
    for i in range (n-1):
        nX = x*math.cos(step) - y*math.sin(step)
        nY = x*math.sin(step) + y*math.cos(step)
        glVertex2f(nX, nY)
        x = nX
        y = nY
    
    #PROBLEM 
    if (n % 2 == 0):
        glRotate(step2 / 2, 0, 0, 1)

    glEnd()
    glFlush()

def main():
    # Initiate GLUT
    glutInit(())
    # Set display attributes
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    # Set window position
    glutInitWindowPosition(80, 80)
    # Set window size
    glutInitWindowSize(500, 500)
    # Create window
    glutCreateWindow("Exercise01")
    # Set callbacks
    glutDisplayFunc(display)
    # Start main loop
    glutMainLoop()

main()
