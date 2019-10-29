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

# Classe do Triangulo
class Triangle3D():
    def __init__(self,x,y,z,width,height):
        self.x = x
        self.y = y
        self.z = z 
        self.width = width
        self.height = height
        self.points = self._create_points()


    def _create_points(self):
        points_list = []
        points_list.append((self.x,self.y, self.z))
        points_list.append((self.x + self.width,self.y, self.z))
        # points_list.append((self.x + self.width,self.y + self.width))
        points_list.append((self.x + self.width/2,self.y + self.height, self.z))
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glColor(0.0,0.0,1.0)
        glVertex3fv(self.points[0])
        glVertex3fv(self.points[1])
        glVertex3fv(self.points[2])

        glEnd()

class Circle3D():
    def __init__(self,x,y, z, base, altura):
        self.x = x
        self.y = y
        self.z = z
        self.base = base
        self.points = self._create_points()
        self.altura = altura

    def _create_points(self):
        points_list = []
        points_list.append((self.x,self.y, self.z))
        points_list.append((self.x + self.radius,self.y, self.z))
        # points_list.append((self.x + self.radius/2,self.y + self.height))
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLE_FAN)

        glColor(0.0,0.0,1.0)
        glVertex3fv(self.points[0])
        i=0
        twoPi = 2*3.1415
        for i in range (1,self.triangles+2):
            glVertex3f((self.radius * math.cos(i *  twoPi / self.triangles)),(self.radius * math.sin(i * twoPi / self.triangles)), self.z)
        
        glEnd()

class Circle3D():
    def __init__(self,x,y,z,radius,triangles):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.points = self._create_points()
        self.triangles = triangles

    def rotate(self, angle): 
        glBegin(GL_TRIANGLE_FAN)

        glColor(0.0,0.0,1.0)
        glVertex3fv(self.points[0])
        i=0
        twoPi = 2*3.1415
        for i in range (1,self.triangles+2):
            glVertex3f((self.radius * math.cos(i *  twoPi / self.triangles)),(self.radius * math.sin(i * twoPi / self.triangles)), self.z )
        
        glEnd()

    def _create_points(self):
        points_list = []
        points_list.append((self.x,self.y, self.z))
        points_list.append((self.x + self.radius,self.y, self.z))
        # points_list.append((self.x + self.radius/2,self.y + self.height))
        return points_list

    def draw(self):
        glBegin(GL_TRIANGLE_FAN)

        glColor(0.0,0.0,1.0)
        glVertex3fv(self.points[0])
        i=0
        twoPi = 2*3.1415
        for i in range (1,self.triangles+2):
            glVertex3f((self.radius * math.cos(i *  twoPi / self.triangles)),(self.radius * math.sin(i * twoPi / self.triangles)), self.z)
        
        glEnd()


    