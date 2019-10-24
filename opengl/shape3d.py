from OpenGL.GL import *
import math

# Classe da Reta
class Reta():
  def __init__(self, begin, end):
    self.begin = begin
    self.end = end
    self.points = self._create_points()

  def _create_points(self):
    points_list = []
    points_list.append(self.begin)
    points_list.append(self.end)  
    return points_list

  def draw(self):
    glBegin(GL_LINE_STRIP)

    glColor(0.0,0.0,1.0)
    glVertex3fv(self.points[0])
    glVertex3fv(self.points[1])

    glEnd()
