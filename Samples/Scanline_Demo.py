# ---------------------------------------------------------------
# Scanline_Demo.py
# ---------------------------------------------------------------

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# --> Uncomment one of the following lines before executing <--

#vertices = [[200,100],[100,-200],[-200,-100],[-100,200]]
#vertices = [[150,100],[100,-200],[-150,-100],[-100,200]]
#vertices = [[200,0],[0,-200],[-200,-0],[-0,200]]
#vertices = [[200,0],[0,-200],[-200,-0]]
vertices = [[150,100],[100,-200],[-150,-100],[-100,200],[0,0]]

def sgn(x):
    if(x < 0):
        result = -1
    else:
        result = 1
    return result

def scanline(v):
    n = len(v)
    pts = []
    p1 = v[0]
    p2 = v[1]
    for i in range(n):
        p3 = v[(i+2) % n]
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if (dy != 0):
            m = dx / dy
            x = p1[0]
            for y in range(p1[1],p2[1],sgn(dy)):
                pts.append([y,x])
                x = x + m * sgn(dy)
            if(dy * (p3[1]-p2[1]) <= 0):
                pts.append([p2[1],x])
        p1 = p2
        p2 = p3
    pts.sort()
    glColor3f(1,0,0)
    glBegin(GL_LINES)
    for i in range(0,len(pts)-1,2):
        #print(pts[i],pts[i+1])
        glVertex2f(pts[i][1],pts[i][0])
        glVertex2f(pts[i+1][1],pts[i+1][0])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Drawing code here
    scanline(vertices)
    glColor3f(1,1,1)
    glBegin(GL_LINE_LOOP)
    for i in range(len(vertices)):
        glVertex2fv(vertices[i])
    glEnd()
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-250,250,-250,250)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Orthographic Sample")
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()