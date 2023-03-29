#Arjun Suresh (AJ) 
#Project 1
#02/02/2023
#Purpose is to create a Hypotrochoid
import math 
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():

    # User Inputs
    # Distance
    d = int(input("Enter d value: "))
    # Small Radius
    r = int(input("Enter r value: "))
    # Big Radius
    bigR = int(input("Enter R value: "))

  # Starting points
    x = 0 
    y = 0

    # Calculate radians
    nD = d*(math.pi/180)
    nr = r*(math.pi/180)
    nR = bigR*(math.pi/180)

    # Theta Calculation for drawing
    #theta2 = (math.lcm(r, bigR))
    theta3 = (2 * math.pi * (float(math.lcm(r, bigR))/bigR))
    theta1 = 0.0

    # Draw the line loop
    glBegin(GL_LINE_LOOP) 
    # Loop while theta is less than theta3
    while(theta1 < theta3):
        # Equation to find the new x and y
        nX = (nr - nR)*math.cos(theta1) + nD * math.cos(((nr - nR) / (nR)) * theta1) 
        nY = (nr - nR)*math.sin(theta1) - nD * math.sin(((nr - nR) / (nR)) * theta1)
        # Set new x and y
        x = nX
        y = nY
        # Draw coordinates after new coordinates are set
        glVertex2f(x,y)
        theta1 += 0.5
    # Finish drawing
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
    glutCreateWindow("Project1 AJ")
    # Set callbacks
    glutDisplayFunc(display)
    # Start main loop
    glutMainLoop()



main()