# Project 2
# Arjun Suresh
# 2/26/2023

#To create a program that will draw a set of polygons using the Painter's Algorithm, an algorithm for visible surface determination 
# in 3D computer graphics that works on a polygon-by-polygon basis rather than a pixel-by-pixel, row by row, or area by area basis of other Hidden Surface Removal algorithms.

#Conceptually Painter's Algorithm works as follows:
    # - Sort each polygon by depth
    # - Render each polygon from the farthest polygon to the closest polygon

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

#Scanline Painter's algorithm code helped from samples (Scanline Demo.py)
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
                #Find Z Coordinates:
                z = p1[2] + (p2[2] - p1[2]) * (y - p1[1]) / (p2[1] - p1[1]) 
                pts.append([y, x, z])
                x += m * sgn(dy)
            if (dy * (p3[1]-p2[1]) <= 0):
                z = p1[2] + (p2[2] - p1[2]) * (p2[1] - p1[1]) / (p2[1] - p1[1]) 
                pts.append([p2[1], x, z])
        p1 = p2
        p2 = p3
    pts.sort()
    glBegin(GL_LINES)
    for i in range(0, len(pts)-1, 2):
        #glVertex3f for 3D Polygons
        glVertex3f(pts[i][1], pts[i][0], pts[i][2]) 
        glVertex3f(pts[i+1][1], pts[i+1][0], pts[i+1][2])
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
            print(polygon[0])
        elif (polygon[1]):
            print(polygon[0])
        elif (polygon[2]):
            print(polygon[0])
            
        glEnd()
        
    glFlush()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Project 2 AJ")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutMainLoop()

main()