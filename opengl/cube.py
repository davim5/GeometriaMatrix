import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
  (1,1,1), #A
  (-1,1,1), #B
  (1,1,-1), #C
  (-1,1,-1), #D
  (1,-1,1), #E
  (-1,-1,1), #F
  (1,-1,-1), #G
  (-1,-1,-1), #H
)

edges = (
  (0,1),
  (0,2),
  (0,4),
  (1,3),
  (1,5),
  (2,3),
  (2,6),
  (3,7),
  (4,5),
  (4,6),
  (5,7),
  (6,7),
)


def cube():
  glBegin(GL_LINES)
  for edge in edges:
    for vertex in edge:
      glVertex3fv(vertices[vertex])
  glEnd( )

if __name__ == "__main__":
  pygame.init()
  display = (500,500)
  pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
  gluPerspective(45,display[0]/display[1],0.1,50.0)
  glTranslate(0.0,0.0,-5)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    glRotate(1,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cube()

    pygame.display.flip()
    pygame.time.wait(10)