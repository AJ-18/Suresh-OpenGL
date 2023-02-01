import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    # Clear window
    glClear(GL_COLOR_BUFFER_BIT)
    # Set stroke/fill color
    glColor3f(1,0,0)
    # Start shape definition
    glBegin(GL_POLYGON)
    # Add vertices
    glVertex2f(-0.7,-0.5)
    glVertex2f(-0.3,0.5)
    glVertex2f(0.7,0.5)
    glVertex2f(0.3,-0.5)
    # Stop shape definition
    glEnd()
    # Set color
    glColor3f(0,0,1)
    # Draw shape
    glutWireTeapot(0.5)
    # Send to display buffer
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
    glutCreateWindow("Sample_1")
    # Set callbacks
    glutDisplayFunc(display)
    # Start main loop
    glutMainLoop()

main()