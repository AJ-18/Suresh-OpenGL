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
    d = int(input("Enter d value: "))
    r = int(input("Enter r value: "))
    bigR = int(input("Enter R value: "))

    #Starting points
    x = 0
    y = 0

    #Theta Calculation for drawing
    theta1 = 0.0
    #theta2 = (math.lcm(r, R))
    theta3 = (2*math.pi*(float((math.lcm(r, R)))/R))

    #Calculate radians
    nD = d*(math.pi/180)
    nr = r*(math.pi/180)
    nR = bigR*(math.pi/180)

    #Set the value calculated in radians as the variables
    d = nD
    r = nr
    bigR = nR

    #Draw the line loop
    glBegin(GL_LINE_LOOP)

    while (theta1 < theta3):
        nX = 
        nY = 
        x = nX
        y = nY





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
