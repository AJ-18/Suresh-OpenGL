import OpenGL
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    d = int(input("Enter d value: "))
    r = int(input("Enter r value: "))
    R = int(input("Enter R value: "))





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
    glutCreateWindow("Project01")
    # Set callbacks
    glutDisplayFunc(display)
    # Start main loop
    glutMainLoop()

main()
