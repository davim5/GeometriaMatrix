import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from shape2d import Square
from shape2d import Rectangle
from shape2d import Triangle
from shape2d import Circle
from shape2d import Line
from shape3d import Reta
from shape3d import Circle3D
from shape3d import Paralelepipedo3D
from shape3d import Pyramid3D

# def cube():
#   glBegin(GL_LINES)
#   for edge in edges:
#     for vertex in edge:
#       glVertex3fv(vertices[vertex])
#   glEnd( )

if __name__ == "__main__":
  pygame.init()
  display = (720,720)
  pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
  gluPerspective(45,display[0]/display[1],0.1,50.0)
  glTranslate(0.0,0.0,-35)
  square = Square(-10,0,10)
  rectangle = Rectangle(-10,0,20,10)
  triangle = Triangle(-10,0,10,10)
  circle = Circle(0,0,10,10)
  line = Line((0,0),(5,5))
  reta = Reta((0,0,0,),(3,3,3))
  reta2 = Reta((4,4,4),(2,5,3))
  circle3d = Circle3D(-10,0,-10,10,10)
  paralelepipedo3D = Paralelepipedo3D(-5,-5,-5,10,10,10)
  pyramid3D = Pyramid3D(-5,-5,-5,10,10,10)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # square.draw()
    # square.drawTrans2d(0.1,0)
    #square.drawRot2d(0.1)
    # rectangle.draw()
    # rectangle.drawTrans2d(0.1,0)
    # triangle.draw()
    # triangle.drawTrans2d(0.1,0)
    # circle.draw()
    # circle.drawTrans2d(0.1,0)
    # circle.drawScale2d(1.005)
    #line.draw()
    #reta.draw()
    #reta2.draw()
    #circle3d.draw()

    # line.draw()
    #reta.draw()
    #reta2.draw()
    # paralelepipedo3D.draw()
    #pyramid3D.draw()

    # glRotate(0.4, 1, 1 ,1)

    pygame.display.flip()
    pygame.time.wait(10)