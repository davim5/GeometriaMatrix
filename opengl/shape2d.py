from OpenGL.GL import *
import math

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

# Classe do Triangulo
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

# Classe do Círculo
class Circle():
  def __init__(self,x,y,radius,triangles):
    self.x = x
    self.y = y
    self.radius = radius
    self.points = self._create_points()
    self.triangles = triangles


  def _create_points(self):
    points_list = []
    points_list.append((self.x,self.y))
    points_list.append((self.x + self.radius,self.y))
    # points_list.append((self.x + self.radius/2,self.y + self.height))
    return points_list

  def draw(self):
    glBegin(GL_TRIANGLE_FAN)

    glColor(0.0,0.0,1.0)
    glVertex2fv(self.points[0])
    i=0
    twoPi = 2*3.1415
    for i in range (1,self.triangles+2):
      glVertex2f((self.radius * math.cos(i *  twoPi / self.triangles)),(self.radius * math.sin(i * twoPi / self.triangles)))
    
    glEnd()
    