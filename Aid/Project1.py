#-- Marcus Vescio -- Project 1
#-- January 31st 2022
#-- This program draws a Hypotrochoid given a Small Radius, Big Radius, and Distance
import math #-- We need to import the math library in order to use cos and sin
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    #-- Starting Points (x,y)
    x = 0 
    y = 0

    #-- User Inputs (Enter them in Degrees as INTS):
    sr = 15 #Small Radius
    bR = 10 #Big Radius
    distance = 5 #Distance

    #-- Conversions to Radians since Python only takes Radians
    d = distance*(math.pi/180)
    a = sr*(math.pi/180)
    b = bR*(math.pi/180)

    #-- Find where we stop drawing the circle using our radian angle equations
    t2 = (math.lcm(sr, bR))
    t3 = (2*math.pi*(float(t2)/bR))
    t = 0.0

    #-- Begin drawing the line loop
    glBegin(GL_LINE_LOOP) 
    #-- Loop while our original theta is less than the required amount (t3) to draw the Hypotrochoid
    while(t < t3):
        #-- Parametric Equations
        nX = (a-b)*math.cos(t) + d*math.cos(((a-b)/(b))*t) 
        nY = (a-b)*math.sin(t) - d*math.sin(((a-b)/(b))*t)
        x = nX
        y = nY
        #-- Set the new coordinates in Vertex and draw
        glVertex2f(x,y)
        t += 0.5
    #-- End drawing
    glEnd()
    glFlush()

def main():
    # Initiate GLUT
    glutInit(())
    # Set display attributes
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    # Set window position
    glutInitWindowPosition(10, 10)
    # Set window size
    glutInitWindowSize(300, 300)
    # Create window
    glutCreateWindow("Project 1 - Marcus")
    # Set callbacks
    glutDisplayFunc(display)
    # Start main loop
    glutMainLoop()



main()