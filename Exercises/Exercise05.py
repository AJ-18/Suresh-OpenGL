import OpenGL
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    radius = 6
    #radius = int (input("Enter the radius: "))

    height = 0
    y = height
    n = int (input("Enter number of points: "))

    #RADIANS
    step = 6.28319/n
    #DEGREES
    step2 = 360.0/n

    #OPENGL wants degrees, python wants radians

    glBegin(GL_POLYGON)
    #glVertex3f(x, y, z)
    for i in range (n-1):
        x = radius*math.cos(step)
        #nY = x*math.sin(step) + y*math.cos(step)
        z = radius*math.sin(step)
        glVertex3f(x, y, z)
       
    #PROBLEM 
    #if (n % 2 == 0):
       # glRotate(step2 / 2, 0, 0, 1)

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
    glutCreateWindow("Exercise05")
    # Set callbacks
    glutDisplayFunc(display)
    # Start main loop
    glutMainLoop()

main()
