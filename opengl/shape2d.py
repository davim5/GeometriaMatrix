from OpenGL.GL import *

class Square():
  def __init__(self,x,y,width):
    self.x = x
    self.y = y
    self.width = width
    self.points = self._create_points()


  def _create_points(self):
    points_list = []
    points_list.append((self.x,self.y))
    points_list.append((self.x + self.width,self.y))
    points_list.append((self.x + self.width,self.y + self.width))
    points_list.append((self.x,self.y + self.width))
    return points_list

  def draw(self):
    glBegin(GL_TRIANGLES)

    glColor(1.0,0.0,0.0)
    glVertex2fv(self.points[0])
    glVertex2fv(self.points[1])
    glVertex2fv(self.points[2])

    glColor(0.0,1.0,0.0)
    glVertex2fv(self.points[2])
    glVertex2fv(self.points[0])
    glVertex2fv(self.points[3])

    glEnd()
    