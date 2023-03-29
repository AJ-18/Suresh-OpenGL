#Arjun Suresh (AJ) 
#Project 1
#02/02/2023
#Purpose is to create a Hypotrochoid

import OpenGL
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    #User Inputs
    #d = int(input("Enter d value: "))
    #r = int(input("Enter r value: "))
    #bigR = int(input("Enter R value: "))
    
    d = 5
    r = 3
    bigR = 5

    #Starting points
    x = 0
    y = 0

    #Theta Calculation for drawing
    theta1 = 0.0
    #theta2 = (math.lcm(r, bigR))
    theta3 = (2*math.pi*(float((math.lcm(r, bigR)))/bigR))

    #Calculate radians
    nD = d*(math.pi/180)
    nr = r*(math.pi/180)
    nR = bigR*(math.pi/180)

    #Draw the line loop
    glBegin(GL_LINE_LOOP)
    #Loop while theta1 is still less than theta3
    while (theta1 < theta3):
        #Equations to get the x and y
        nX = (nr - nR) * math.cos(theta1) + nD * math.cos(((nr - nR)) / (nR) * theta1)
        nY = (nr - nR) * math.sin(theta1) + nD * math.sin(((nr - nR)) / (nR) * theta1)
        x = nX
        y = nY

        #Draw the actual coordinates after setting the new coordinates.
        glVertex2f(x,y)
        theta1 * 0.5
    #Finish drawing
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
    glutCreateWindow("Project01_AJ")
    # Set callbacks
    glutDisplayFunc(display)
    # Start main loop
    glutMainLoop()

main()
