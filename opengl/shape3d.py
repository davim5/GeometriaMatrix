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


    
class Cube():
  def __init__(self,x,y,z,lado):
    self.x = x
    self.y = y
    self.z = z
    self.lado = lado
    self.points = self.createPoints()
  
  def createPoints(self):
    point_list = []
    point_list.append(((self.x + self.lado),(self.y + self.lado),(self.z + self.lado))) #0
    point_list.append(((self.x - self.lado),(self.y + self.lado),(self.z + self.lado))) #1
    point_list.append(((self.x + self.lado),(self.y + self.lado),(self.z - self.lado))) #2
    point_list.append(((self.x - self.lado),(self.y + self.lado),(self.z - self.lado))) #3
    point_list.append(((self.x + self.lado),(self.y - self.lado),(self.z + self.lado))) #4
    point_list.append(((self.x - self.lado),(self.y - self.lado),(self.z + self.lado))) #5
    point_list.append(((self.x + self.lado),(self.y - self.lado),(self.z - self.lado))) #6
    point_list.append(((self.x - self.lado),(self.y - self.lado),(self.z - self.lado))) #7
    return point_list



  def draw(self):
    glBegin(GL_TRIANGLES)

    glColor(0.0,1.0,0.0)
    glVertex3fv(self.points[0])
    glVertex3fv(self.points[1])
    glVertex3fv(self.points[2])

    glColor(1.0,0.0,0.0)
    glVertex3fv(self.points[1])
    glVertex3fv(self.points[2])
    glVertex3fv(self.points[3])

    glEnd()

class Paralelepipedo3D():
    def __init__(self,x,y,z, largura, comprimento, altura):
        self.x = x
        self.y = y
        self.z = z
        self.largura = largura 
        self.comprimento = comprimento
        self.altura = altura
        self.points = self.createPoints()
    
    def createPoints(self):
        largura = self.largura
        altura = self.altura
        comprimento = self.comprimento 

        point_list = []
        #lado de baixo
        point_list.append(((self.x),(self.y),(self.z))) #1
        point_list.append(((self.x+largura),(self.y),(self.z))) #2
        point_list.append(((self.x),(self.y),(self.z+comprimento))) #3

        point_list.append(((self.x+largura),(self.y),(self.z))) #2
        point_list.append(((self.x),(self.y),(self.z+comprimento))) #3
        point_list.append(((self.x+largura),(self.y),(self.z+comprimento))) #4

        #lado de cima
        point_list.append(((self.x),(self.y+altura),(self.z))) #5
        point_list.append(((self.x+largura),(self.y+altura),(self.z))) #6
        point_list.append(((self.x),(self.y+altura),(self.z+comprimento))) #7

        point_list.append(((self.x+largura),(self.y+altura),(self.z))) #6
        point_list.append(((self.x),(self.y+altura),(self.z+comprimento))) #7
        point_list.append(((self.x+largura),(self.y+altura),(self.z+comprimento))) #8

        #lado da esquerda
        point_list.append(((self.x),(self.y),(self.z))) #1
        point_list.append(((self.x),(self.y),(self.z+comprimento))) #3
        point_list.append(((self.x),(self.y+altura),(self.z))) #5

        point_list.append(((self.x),(self.y),(self.z+comprimento))) #3
        point_list.append(((self.x),(self.y+altura),(self.z))) #5
        point_list.append(((self.x),(self.y+altura),(self.z+comprimento))) #7

        #lado de tras

        point_list.append(((self.x),(self.y),(self.z))) #1
        point_list.append(((self.x+largura),(self.y),(self.z))) #2
        point_list.append(((self.x),(self.y+altura),(self.z))) #5

        point_list.append(((self.x+largura),(self.y),(self.z))) #2
        point_list.append(((self.x),(self.y+altura),(self.z))) #5
        point_list.append(((self.x+largura),(self.y+altura),(self.z))) #6

        #lado da direita
        point_list.append(((self.x+largura),(self.y),(self.z))) #2
        point_list.append(((self.x+largura),(self.y),(self.z+comprimento))) #4
        point_list.append(((self.x+largura),(self.y+altura),(self.z))) #6

        point_list.append(((self.x+largura),(self.y),(self.z+comprimento))) #4
        point_list.append(((self.x+largura),(self.y+altura),(self.z))) #6
        point_list.append(((self.x+largura),(self.y+altura),(self.z+comprimento))) #8

        #lado da frente
        point_list.append(((self.x),(self.y),(self.z+comprimento))) #3
        point_list.append(((self.x+largura),(self.y),(self.z+comprimento))) #4
        point_list.append(((self.x),(self.y+altura),(self.z+comprimento))) #7

        point_list.append(((self.x+largura),(self.y),(self.z+comprimento))) #4
        point_list.append(((self.x),(self.y+altura),(self.z+comprimento))) #7
        point_list.append(((self.x+largura),(self.y),(self.z+comprimento))) #8

        
        return point_list



    def draw(self):
        glBegin(GL_TRIANGLES)

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[0])
        glVertex3fv(self.points[1])
        glVertex3fv(self.points[2])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[3])
        glVertex3fv(self.points[4])
        glVertex3fv(self.points[5])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[6])
        glVertex3fv(self.points[7])
        glVertex3fv(self.points[8])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[9])
        glVertex3fv(self.points[10])
        glVertex3fv(self.points[11])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[12])
        glVertex3fv(self.points[13])
        glVertex3fv(self.points[14])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[15])
        glVertex3fv(self.points[16])
        glVertex3fv(self.points[17])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[18])
        glVertex3fv(self.points[19])
        glVertex3fv(self.points[20])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[21])
        glVertex3fv(self.points[22])
        glVertex3fv(self.points[23])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[24])
        glVertex3fv(self.points[25])
        glVertex3fv(self.points[26])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[27])
        glVertex3fv(self.points[28])
        glVertex3fv(self.points[29])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[30])
        glVertex3fv(self.points[31])
        glVertex3fv(self.points[32])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[33])
        glVertex3fv(self.points[34])
        glVertex3fv(self.points[35])



        glEnd()

class Pyramid3D():
    def __init__(self,x,y,z, largura, comprimento, altura):
        self.x = x
        self.y = y
        self.z = z
        self.largura = largura 
        self.comprimento = comprimento
        self.altura = altura
        self.points = self.createPoints()
    
    def createPoints(self):
        largura = self.largura
        altura = self.altura
        comprimento = self.comprimento 

        point_list = []
        #lado de baixo
        point_list.append(((self.x),(self.y),(self.z))) #1
        point_list.append(((self.x+largura),(self.y),(self.z))) #2
        point_list.append(((self.x),(self.y),(self.z+comprimento))) #3

        point_list.append(((self.x+largura),(self.y),(self.z))) #2
        point_list.append(((self.x),(self.y),(self.z+comprimento))) #3
        point_list.append(((self.x+largura),(self.y),(self.z+comprimento))) #4

        #triang esquerda
        point_list.append(((self.x),(self.y),(self.z))) #1
        point_list.append(((self.x),(self.y),(self.z + comprimento))) #3
        point_list.append(((self.x + (largura/2)),(self.y+altura),(self.z+(comprimento/2)))) #5


        #triang tras
        point_list.append(((self.x),(self.y),(self.z))) #1
        point_list.append(((self.x + largura),(self.y),(self.z))) #2
        point_list.append(((self.x + (largura/2)),(self.y+altura),(self.z+(comprimento/2)))) #5


        #triang direita

        point_list.append(((self.x + largura),(self.y),(self.z))) #2
        point_list.append(((self.x+largura),(self.y),(self.z + comprimento))) #4
        point_list.append(((self.x + (largura/2)),(self.y+altura),(self.z+(comprimento/2)))) #5


        #triango frente
        point_list.append(((self.x),(self.y),(self.z+comprimento))) #3
        point_list.append(((self.x+largura),(self.y),(self.z + comprimento))) #4
        point_list.append(((self.x + (largura/2)),(self.y+altura),(self.z+(comprimento/2)))) #5

        
        
        return point_list



    def draw(self):
        glBegin(GL_TRIANGLES)

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[0])
        glVertex3fv(self.points[1])
        glVertex3fv(self.points[2])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[3])
        glVertex3fv(self.points[4])
        glVertex3fv(self.points[5])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[6])
        glVertex3fv(self.points[7])
        glVertex3fv(self.points[8])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[9])
        glVertex3fv(self.points[10])
        glVertex3fv(self.points[11])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[12])
        glVertex3fv(self.points[13])
        glVertex3fv(self.points[14])

        glColor(0.0,1.0,0.0)
        glVertex3fv(self.points[15])
        glVertex3fv(self.points[16])
        glVertex3fv(self.points[17])

        



        glEnd()





