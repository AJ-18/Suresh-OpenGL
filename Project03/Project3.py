# Project 3
# Arjun Suresh
# 3/28/2023

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

#Added colors to distinguish each shape

def drawWireCylinder(radius1, radius2, height):
    segments = 32
    #Exercise 5 helped with some code.

    #Calculate angle
    theta = (2 * math.pi) / segments
    
    #Calculate top part of the cylinder
    glBegin(GL_LINE_LOOP)
    
    for i in range(segments):
        x = radius1 * math.cos(i * theta)
        z = radius1 * math.sin(i * theta)
        glVertex3f(x, height/2, z)
        
    glEnd()
    
    
    #Calculate bottom part of cylinder
    glBegin(GL_LINE_LOOP)
    
    for i in range(segments):
        x = radius2 * math.cos(i * theta)
        z = radius2 * math.sin(i * theta)
        glVertex3f(x, -height/2, z)
        
    glEnd()
    
    
    #Draw the sides of the cylinder
    glBegin(GL_LINE_LOOP) #GL LINE also works
    
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
    gluLookAt(0, 0, 6, 0, 0, 0, 0, 1, 0) #Change the view

    #Cone
    drawWireCylinder(0, 1.7, 3)

    #Sphere
    glPushMatrix()
    glTranslatef(0, -0.9, 0)
    glColor3f(1, 1, 0)
    glutWireSphere(1.5, 30, 30)
    glPopMatrix()
 
    #Cylinder
    glPushMatrix()
    glTranslatef(0, 1, 0)
    glRotatef(90, 1, 1, 0)
    glTranslatef(0, 0, 1.1)
    glColor3f(1, 0, 1)
    drawWireCylinder(0.8, 0.8, 2)
    glPopMatrix()
    glFlush()


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