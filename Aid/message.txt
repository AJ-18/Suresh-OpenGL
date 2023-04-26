#-- Marcus Vescio -- Project 4
#-- April 24th 2022
#-- Modified the program Curved_Surface.py as follows:
# -- -Instead of drawing GL_LINE_STRIP's, the program will use glEvalCoord2f() to create GL_QUADS.
#--  -Each call to glEvalCoord2f() is preceded with a call to glTexCoord2f(u,v) using the same values for u and v as for glEvalCoord2f().
#--  -Implement texture mapping to texture the surface. (Image file chosen is brick.jpg chosen for simplicity)
#--  -Light source included
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

#-- Draw Controls
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

#-- Draw Surface Function
def drawSurface():
   steps = 17 #Imported from Curved_Surfaces, steps taken for first for loop
   steps2 = 31 #Steps taken for second for loop
   for i in range(steps):
      glBegin(GL_QUADS) #Changed to GL_QUADS
      for j in range(steps2): #Used values u, v as requested
            u = j/steps2 
            v = i/steps
            glTexCoord2f(u,v) #Each EvalCoord cal is preceded by a TexCoord cal
            glEvalCoord2f(u, v)
            u = (j+1) / steps2
            v = i / steps
            glTexCoord2f(u,v)
            glEvalCoord2f(u, v)
            u = (j+1)/steps2
            v = (i+1)/steps
            glTexCoord2f(u,v)
            glEvalCoord2f(u, v)
            u = j/steps2
            v = (i+1)/steps
            glTexCoord2f(u, v)
            glEvalCoord2f(u, v)
      glEnd()
   glDisable(GL_TEXTURE_2D)   

#-- Read Texture imported from Texture2.py. Read the brick texture using pillow and numpy
def read_texture(filename):
    img = Image.open(filename).convert("L")
    img_data = numpy.array(list(img.getdata()), numpy.int16)
    img_data = img_data.reshape(img.size[1], img.size[0])
    textID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glGenTextures(1, 0)
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
   tex = read_texture("brick.jpg") #Brick texture
   glEnable(GL_TEXTURE_2D)
   glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
   glBindTexture(GL_TEXTURE_2D, tex)
   glPushMatrix()
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
   glutCreateWindow("Project 4 - Marcus")
   glEnable(GL_LIGHTING)
   lightZeroPosition = [10., 4., 10., 1.]
   lightZeroColor = [0.8, 1.0, 0.8, 1.0]
   glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
   glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
   glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
   glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
   glEnable(GL_LIGHT0)
   glutDisplayFunc(display)
   init()
   glutMainLoop()

main()