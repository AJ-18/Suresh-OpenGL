#Arjun Suresh (AJ)
#Project 4


from OpenGL.GL   import *
from OpenGL.GLUT import *
from OpenGL.GLU  import *
from PIL import Image as Image
import numpy

ctrlpoints = [
   [[-1.5, -1.5,  4.0], [-0.5, -1.5,  2.0], [0.5, -1.5, -1.0], [1.5, -1.5,  2.0]], 
   [[-1.5, -0.5,  1.0], [-0.5, -0.5,  3.0], [0.5, -0.5,  0.0], [1.5, -0.5, -1.0]], 
   [[-1.5,  0.5,  4.0], [-0.5,  0.5,  0.0], [0.5,  0.5,  3.0], [1.5,  0.5,  4.0]], 
   [[-1.5,  1.5, -2.0], [-0.5,  1.5, -2.0], [0.5,  1.5,  0.0], [1.5,  1.5, -1.0]]
   ]

# #def drawControls():
#    glColor3f(1.0, 0.0, 0.0)
#    glPushMatrix()
#    for i in range(4):
#       glBegin(GL_LINE_STRIP)
#       for j in range(4):
#          glVertex3fv(ctrlpoints[i][j])
#       glEnd()
#    for i in range(4):
#       glBegin(GL_LINE_STRIP)
#       for j in range(4):
#          glVertex3fv(ctrlpoints[j][i])
#       glEnd()
#    glPopMatrix()

# Use u in outer loop, v in inner loop - use it to find point one
# Use offsets to find other 3 points

def drawSurface():
   glColor3f(1.0, 1.0, 1.0)
   glPushMatrix()
   for j in range(31): # u direction - Outer loop
      glBegin(GL_QUADS)
      for i in range(17): # v direction - Inner loop
         u = j/31.0
         v = i/17.0
         glTexCoord2f(u, v)
         glEvalCoord2f(u, v)
         
         #Offset just u value
         u = ( j + 1 ) / 31
         v = i / 17
         glTexCoord2f(u, v)
         glEvalCoord2f(u, v)

         #Offset u and v value
         u = ( j + 1 ) / 31
         v = ( i + 1 ) / 17
         glTexCoord2f(u, v)
         glEvalCoord2f(u, v)

        #Offset just v value
         u = j / 31
         v = ( i + 1 ) / 17
         glTexCoord2f(u, v)
         glEvalCoord2f(u, v)

      glEnd()
   glPopMatrix()

#Imported read texture from the texture2 sample
def read_texture(filename):
    img = Image.open(filename)
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    textID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glGenTextures(1, 0);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB,
                 GL_UNSIGNED_BYTE, img_data)
    return textID

def display():
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   tex = read_texture("brick.jpg") #The brick texture
   glEnable(GL_TEXTURE_2D)
   glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
   glBindTexture(GL_TEXTURE_2D, tex)
   glPushMatrix()
   glRotatef(45,1,1,1)
   #drawControls()
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
    glutCreateWindow("Project 4 AJ")
    glutDisplayFunc(display)
    init()
    glutMainLoop()


main()