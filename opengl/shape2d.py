from OpenGL.GL import *
import math

# Classe da linha
class Line():
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
    glVertex2fv(self.points[0])
    glVertex2fv(self.points[1])

    glEnd()

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

  def drawTrans2d(self,tx,ty):
    self.x += tx
    self.y += ty
    self.points = self._create_points()  
    self.draw()

  def drawScale2d(self,ts):
    self.width *= ts
    self.points = self._create_points()  
    self.draw()

  def drawRot2d(self,angle):
    
    self.x = self.x*math.cos(angle) - self.y*math.sin(angle)
    self.y = self.x*math.sin(angle) + self.y*math.cos(angle)
    self.points = self._create_points()  
    self.draw()
    

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

  def drawTrans2d(self,tx,ty):
    self.x += tx
    self.y += ty
    self.points = self._create_points()  
    self.draw()
  
  def drawScale2d(self,ts):
    self.width *= ts
    self.height *= ts
    self.points = self._create_points()  
    self.draw()


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

  def drawTrans2d(self,tx,ty):
    self.x += tx
    self.y += ty
    self.points = self._create_points()  
    self.draw()

  def drawScale2d(self,ts):
    self.width *= ts
    self.height *= ts
    self.points = self._create_points()  
    self.draw()

# Classe do Circulo
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
      sx = (self.radius * math.cos(i *  twoPi / self.triangles))
      sy = (self.radius * math.sin(i * twoPi / self.triangles))

      X =  (sx - self.x)*math.cos(self.angle) - (sy - self.y)*math.sin(self.angle)
      Y =  (sx - self.x)*math.sin(self.angle) + (sy - self.y)*math.cos(self.angle)
      glVertex2f((self.x + X) - self.radius, (self.y + Y) - self.radius)
    
    glEnd()
    
  def drawTrans2d(self,tx,ty):
    self.x += tx
    self.y += ty
    self.points = self._create_points()  
    self.draw()

  def drawScale2d(self,ts):
    self.radius *= ts
    self.points = self._create_points()  
    self.draw()
