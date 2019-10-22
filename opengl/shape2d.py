from OpenGL.GL import *

# Classe do quadrado
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

    glColor(0.0,0.0,1.0)
    glVertex2fv(self.points[0])
    glVertex2fv(self.points[1])
    glVertex2fv(self.points[2])

    glColor(0.0,1.0,0.0)
    glVertex2fv(self.points[2])
    glVertex2fv(self.points[0])
    glVertex2fv(self.points[3])

    glEnd()

# Classe do retangulo
class Rectangle():
  def __init__(self,x,y,width,height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.points = self._create_points()


  def _create_points(self):
    points_list = []
    points_list.append((self.x,self.y))
    points_list.append((self.x + self.width,self.y))
    points_list.append((self.x + self.width,self.y + self.height))
    points_list.append((self.x,self.y + self.height))
    return points_list

  def draw(self):
    glBegin(GL_TRIANGLES)

    glColor(0.0,0.0,1.0)
    glVertex2fv(self.points[0])
    glVertex2fv(self.points[1])
    glVertex2fv(self.points[2])

    glColor(0.0,1.0,0.0)
    glVertex2fv(self.points[2])
    glVertex2fv(self.points[0])
    glVertex2fv(self.points[3])

    glEnd()

# Classe do quadrado
class Triangle():
  def __init__(self,x,y,width,height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.points = self._create_points()


  def _create_points(self):
    points_list = []
    points_list.append((self.x,self.y))
    points_list.append((self.x + self.width,self.y))
    # points_list.append((self.x + self.width,self.y + self.width))
    points_list.append((self.x + self.width/2,self.y + self.height))
    return points_list

  def draw(self):
    glBegin(GL_TRIANGLES)

    glColor(0.0,0.0,1.0)
    glVertex2fv(self.points[0])
    glVertex2fv(self.points[1])
    glVertex2fv(self.points[2])

    glEnd()
    