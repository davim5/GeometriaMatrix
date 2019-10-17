import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from shape2d import Square

# def cube():
#   glBegin(GL_LINES)
#   for edge in edges:
#     for vertex in edge:
#       glVertex3fv(vertices[vertex])
#   glEnd( )

if __name__ == "__main__":
  pygame.init()
  display = (500,500)
  pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
  gluPerspective(45,display[0]/display[1],0.1,50.0)
  glTranslate(0.0,0.0,-35)
  square = Square(1,1,10)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    square.draw()

    pygame.display.flip()
    pygame.time.wait(10)