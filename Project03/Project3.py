# Project 3
# Arjun Suresh
# 3/28/2023

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

#No colors, change numbers of shape, but be accurate to original shape, omit segments(Make segments a global variable, make it 32) - Maybe change gluPerspective (keep aspect ratio), change transformations

def drawWireCylinder(radius1, radius2, height, segments): #-- I added a segments parameter for the user be able to pick how many segments the cylinder is divided into. (The higher the number, the more the segments)
    segments = 32
    #-- Some code imported from my Exercise 5 assignment since we were drawing cylinders in that exercise.
    # Note to self: height represents our Y, use that when executing glVertex3f 

    #-- Calculate angle between each segment
    theta = (2 * math.pi) / segments
    
    #-- Top circle of cylinder (Radius1)
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        x = radius1 * math.cos(i * theta)
        z = radius1 * math.sin(i * theta)
        glVertex3f(x, height/2, z)
    glEnd()
    
    #-- Bottom circle of cylinder (Radius2)
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        x = radius2 * math.cos(i * theta)
        z = radius2 * math.sin(i * theta)
        glVertex3f(x, -height/2, z)
    glEnd()
    
    #-- Drawing the sides of the cylinder connected to the two radii
    glBegin(GL_LINES) #Can change to Line Loop
    for i in range(segments):
        x1 = radius1 * math.cos(i * theta)
        x2 = radius2 * math.cos(i * theta)
        z1 = radius1 * math.sin(i * theta)
        z2 = radius2 * math.sin(i * theta)
        glVertex3f(x1, height/2, z1)
        glVertex3f(x2, -height/2, z2)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 7, 0, 0, 0, 0, 1, 0) #Front-facing, to make an overhead view change it to 7, 7, 7 instead of 0, 0, 7 - Change the 3rd parameter

    #-- Shape 1 (Cone) 
    drawWireCylinder(0, 1.5, 3, 24) #Change 

    #-- Shape 2 (Sphere) - Change translation?
    glPushMatrix()
    glTranslatef(0, -0.5, 0)
    glColor3f(1, 0, 0)
    glutWireSphere(1.5, 30, 30)
    glPopMatrix()
 
    #-- Shape 3 (Cylinder)
    glPushMatrix()
    glTranslatef(0, 1, 0)
    glRotatef(90, 1, 1, 0)
    glTranslatef(0, 0, 1)
    glColor3f(0, 0, 1)
    drawWireCylinder(0.8, 0.8, 2, 24)
    glPopMatrix()
    glFlush()

    #Sidenote: Tried to make shapes and their transformations identical to those shown in image.

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 100)

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Project 3 AJ")
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()