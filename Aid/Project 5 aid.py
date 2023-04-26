import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
LINK_LENGTH = 0.2
LINK_WIDTH = 0.05
GRAVITY = 9.81
INITIAL_ANGLE = np.pi / 4
TIME_STEP = 0.01

# Define variables
angle = INITIAL_ANGLE
angular_velocity = 0.0
angular_acceleration = 0.0

# Define functions
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(WINDOW_WIDTH)/float(WINDOW_HEIGHT), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_link():
    glBegin(GL_QUADS)
    glVertex3f(-LINK_WIDTH/2, 0.0, 0.0)
    glVertex3f(LINK_WIDTH/2, 0.0, 0.0)
    glVertex3f(LINK_WIDTH/2, LINK_LENGTH, 0.0)
    glVertex3f(-LINK_WIDTH/2, LINK_LENGTH, 0.0)
    glEnd()

def draw_chain():
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    draw_link()
    for i in range(4):
        glTranslatef(0.0, LINK_LENGTH, 0.0)
        draw_link()
    glPopMatrix()

def update():
    global angle, angular_velocity, angular_acceleration
    angular_acceleration = -GRAVITY/LINK_LENGTH * np.sin(angle)
    angular_velocity += angular_acceleration * TIME_STEP
    angle += angular_velocity * TIME_STEP

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glRotatef(np.degrees(angle), 0.0, 0.0, 1.0)
    draw_chain()
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)

def idle():
    update()
    glutPostRedisplay()

# Main program
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutCreateWindow("Swinging Chain")
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutIdleFunc(idle)
glutMainLoop()
