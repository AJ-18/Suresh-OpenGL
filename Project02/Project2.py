# Project 2
# Arjun Suresh
# 2/26/2023

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Polygon's defined
polygon1 = [[100,100,2],[100,200,2],[200,100,2]]
polygon2 = [[-50,-50,10],[150,150,10],[-50,150,10]]
polygon3 = [[-100,-10,5],[200,-10,5],[200,10,5]]

# Polygon list
polygons = [polygon1, polygon2, polygon3]

def sgn(x):
    if(x < 0):
        result = -1
    else:
        result = 1
    return result

def scanline(polygon):
    n = len(polygon)
    pts = []
    p1 = polygon[0]
    p2 = polygon[1]
    for i in range(n):
        p3 = polygon[(i+2) % n]
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if dy != 0:
            m = dx / dy
            x = p1[0]
            for y in range(p1[1], p2[1], sgn(dy)):
                z = p1[2] + (p2[2] - p1[2]) * (y - p1[1]) / (p2[1] - p1[1]) #How to find z coordinates
                pts.append([y, x, z]) #Need to add new z coordinate to append
                x += m * sgn(dy)
            if (dy * (p3[1]-p2[1]) <= 0):
                z = p1[2] + (p2[2] - p1[2]) * (p2[1] - p1[1]) / (p2[1] - p1[1]) 
                pts.append([p2[1], x, z]) #Need to add new z coordinate to append
        p1 = p2
        p2 = p3
    pts.sort()
    glBegin(GL_LINES)
    for i in range(0, len(pts)-1, 2):
        glVertex3f(pts[i][1], pts[i][0], pts[i][2]) #We are using glVertex3f now instead of 2f since we have a z coordinate now (3D Polygon now)
        glVertex3f(pts[i+1][1], pts[i+1][0], pts[i+1][2]) #We are using glVertex3f now instead of 2f since we have a z coordinate now (3D Polygon now)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -250, 250, 1, 20)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 20, 0, 0, 0, 0, 1, 0)
    for polygon in polygons:
        scanline(polygon)
        glBegin(GL_POLYGON)
        for vertex in polygon:
            glVertex3fv(vertex)
        if (polygon[0]):
            glColor3f(1, 0, 0) # set color to red
            print(polygon[0])
        elif (polygon[1]):
            glColor3f(0, 1, 0) # set color to green
            print(polygon[0])
        elif (polygon[2]):
            glColor3f(0, 0, 1) # set color to blue
            print(polygon[0])
        glEnd()
    glFlush()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Painters Algorithm")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutMainLoop()

main()