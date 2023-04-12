from OpenGL.GL   import *
from OpenGL.GLUT import *
from OpenGL.GLU  import *

ctrlpoints = [
   [[-1.5, -1.5,  4.0], [-0.5, -1.5,  2.0], [0.5, -1.5, -1.0], [1.5, -1.5,  2.0]], 
   [[-1.5, -0.5,  1.0], [-0.5, -0.5,  3.0], [0.5, -0.5,  0.0], [1.5, -0.5, -1.0]], 
   [[-1.5,  0.5,  4.0], [-0.5,  0.5,  0.0], [0.5,  0.5,  3.0], [1.5,  0.5,  4.0]], 
   [[-1.5,  1.5, -2.0], [-0.5,  1.5, -2.0], [0.5,  1.5,  0.0], [1.5,  1.5, -1.0]]
   ]

def drawControls():
   glColor3f(1.0, 0.0, 0.0)
   glPushMatrix()
   for i in range(4):
      glBegin(GL_LINE_STRIP)
      for j in range(4):
         glVertex3fv(ctrlpoints[i][j])
      glEnd()
   for i in range(4):
      glBegin(GL_LINE_STRIP)
      for j in range(4):
         glVertex3fv(ctrlpoints[j][i])
      glEnd()
   glPopMatrix()

def drawSurface():
   glColor3f(1.0, 1.0, 1.0)
   glPushMatrix()
   for j in range(17):
      glBegin(GL_LINE_STRIP)
      for i in range(31):
         glEvalCoord2f(i/30.0, j/16.0)
      glEnd()
      glBegin(GL_LINE_STRIP)
      for i in range(31):
         glEvalCoord2f(j/16.0, i/30.0)
      glEnd()
   glPopMatrix()

def display():
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glRotatef(45,1,1,1)
   drawControls()
   drawSurface()
   glFlush()

def init():
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glColor3f(1.0, 1.0, 1.0)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   gluPerspective(60,1,1,20)
   gluLookAt(0,0,-10,0,0,0,0,1,0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, ctrlpoints)
   glEnable(GL_MAP2_VERTEX_3)
   glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
   glEnable(GL_DEPTH_TEST)
   glShadeModel(GL_FLAT)

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow("Curved Surface Example")
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()