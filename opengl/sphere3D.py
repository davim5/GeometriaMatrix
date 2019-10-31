
from OpenGL.GL import *
from OpenGL.GLU import *
import sys, pygame, math
from pygame.locals import *

#iniciando o pygame
pygame.init( )

# setando as dimensões da janela
scr_size = ( 800, 600 )  # primeiro é largura, segundo é largura
screen = pygame.display.set_mode( scr_size, FULLSCREEN | HWSURFACE | OPENGL | DOUBLEBUF )
pygame.display.set_caption( "Esfera triangulada!" )

# globais
clock = pygame.time.Clock()
ROTANGLE = 0
SRADIUS = 2
SDEPTH = 1
SID = 0
LIGHTS = False
WHITE = [ 1.0, 1.0, 1.0, 0.0 ]
GREY = [ .3, .3, .3, 0 ]
RED = [ 1.0, 0.0, 0.0, 0.0 ]
SPEC = [ 0.9, 0.9, 0.9, 1.0 ]
LIGHTPOS = [ 4, 2, 2, 0 ]


def lights_setup( ):
    # Configurando as etapas de processamento apropriadas para iluminação.
    glEnable( GL_DEPTH_TEST ) 
    glEnable( GL_NORMALIZE )

    # fonte de luz.
    glLightfv( GL_LIGHT0, GL_POSITION, LIGHTPOS )   
    glLightfv( GL_LIGHT0, GL_DIFFUSE, WHITE ) 
    glLightfv( GL_LIGHT0, GL_AMBIENT, GREY ) 
    glLightfv( GL_LIGHT0, GL_SPECULAR, SPEC )
    glEnable( GL_LIGHT0 ) 

def lights_on( on ):
    if on:
        glPolygonMode( GL_FRONT, GL_FILL )
        glEnable( GL_LIGHTING )
    else:
        glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )
        glDisable( GL_LIGHTING )

def init_gl( w, h ):  
    # limpando a tela e estados definidos
    glClearColor( 0.0, 0.0, 0.0, 0.0 )                   
    glClearDepth( 1.0 )
    glDepthFunc( GL_LESS )
    glEnable( GL_DEPTH_TEST )

    # iluminação
    glShadeModel( GL_SMOOTH )
    glEnable(GL_COLOR_MATERIAL)    
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)        
    glLight(GL_LIGHT0, GL_POSITION,  (0, 1, 1, 0))  
    
    # setando a projeção
    glMatrixMode( GL_PROJECTION )
    glLoadIdentity( )
    gluPerspective( 45.0, float( w )/h, 0.1, 100.0 )
    glMatrixMode( GL_MODELVIEW )

# a função é chamada quando a janela é redimensionada (o que não deve acontecer se você ativar a tela cheia)
def resize( w, h ):
    glViewport( 0, 0, w, h )
    glMatrixMode (GL_PROJECTION )
    glLoadIdentity( )
    gluPerspective( 45.0, float(w)/h, 0.1, 100.0 )
    glMatrixMode( GL_MODELVIEW )
    glLoadIdentity( )

def projection( w, h ):
    glMatrixMode( GL_PROJECTION )
    gluPerspective( 45.0, float(w)/h, .1, 100.0 )
    gluLookAt( 0.0,0.0,10.0, 0.0,0.0,0.0, 0.0,1.0,0.0 )

#normalize
def normalize( vector ):
  a, b, c = vector
  length = math.sqrt( a**2 + b**2 + c**2 )
  if length != 0:
    return [ a/length, b/length, c/length ]
  return [ 0.0, 0.0, 0.0 ]
#-------------------------------------------------------end normalize

 # p1 e p2 são passados ​​na ordem "anti-horária" a partir do desenho opengl
def midpoint( p1, p2 ):
    return [ ( p1[ 0 ] + p2[ 0 ] )/2.0, ( p1[ 1 ] + p2[ 1 ] )/2.0, ( p1[ 2 ] + p2[ 2 ] )/2.0 ]

def midbump( p1, p2, radius ):
    m = normalize( midpoint( p1, p2 ) )
    return [ m[ 0 ]*radius, m[ 1 ]*radius, m[ 2 ]*radius ]

def rec_sphere( radius, depth, tri, trilist ):
    if depth == 0:
        trilist.append( tri )
        return
    
    #obter pontos médios da linha e mover para a borda da esfera
    m1 = midbump( tri[ 0 ], tri[ 1 ], radius )
    m2 = midbump( tri[ 1 ], tri[ 2 ], radius )
    m3 = midbump( tri[ 2 ], tri[ 0 ], radius )

    # fazendo os novos triângulos
    face = [ tri[ 0 ], m1, m3 ]
    rec_sphere( radius, depth-1, face, trilist )
    face = [ m1, tri[ 1 ], m2 ]
    rec_sphere( radius, depth-1, face, trilist )
    face = [ m2, tri[ 2 ], m3 ]
    rec_sphere( radius, depth-1, face, trilist )
    face = [ m1, m2, m3 ]
    rec_sphere( radius, depth-1, face, trilist )

def gen_sphere( radius, depth ):
    global SID
    #os pontos médios da linha de diamante na superfície da esfera para cada face
    trilist = []
    radius = float( radius )
    face = [ ( 0.0, radius, 0.0 ), ( -radius, 0.0, 0.0 ), ( 0.0, 0.0, radius ) ]
    rec_sphere( radius, depth-1, face, trilist )
    face = [ ( 0.0, radius, 0.0 ), ( 0.0, 0.0, radius ), ( radius, 0.0, 0.0 ) ]
    rec_sphere( radius, depth-1, face, trilist )
    face = [ ( 0.0, radius, 0.0 ), ( radius, 0.0, 0.0 ), ( 0.0, 0.0, -radius ) ]
    rec_sphere( radius, depth-1, face, trilist )
    face = [ ( 0.0, radius, 0.0 ), ( 0.0, 0.0, -radius ), ( -radius, 0.0, 0.0 ) ]
    rec_sphere( radius, depth-1, face, trilist )
    #metade inferior do diamante
    face = [ ( 0.0, -radius, 0.0 ), ( 0.0, 0.0, radius ), ( -radius, 0.0, 0.0 ) ]
    rec_sphere( radius, depth-1, face, trilist )
    face = [ ( 0.0, -radius, 0.0 ), ( radius, 0.0, 0.0 ), ( 0.0, 0.0, radius ) ]
    rec_sphere( radius, depth-1, face, trilist )
    face = [ ( 0.0, -radius, 0.0 ), ( 0.0, 0.0, -radius ), ( radius, 0.0, 0.0 ) ]
    rec_sphere( radius, depth-1, face, trilist )
    face = [ ( 0.0, -radius, 0.0 ), ( -radius, 0.0, 0.0 ), ( 0.0, 0.0, -radius ) ]
    rec_sphere( radius, depth-1, face, trilist )

    # criando a lista de chamadas e atraia para ela
    SID = glGenLists( 1 )
    glNewList( SID, GL_COMPILE )
    glBegin( GL_TRIANGLES )
    for tri in trilist:
        for vert in tri:
            glNormal3dv( normalize( vert ) )
            glVertex3dv( vert )
    glEnd( )
    glEndList( )
    
def draw_sphere( ):
    glMatrixMode( GL_MODELVIEW ) 
    glPushMatrix( )
    glLoadIdentity( )
    glRotatef( ROTANGLE, 0.0,1.0,0.0 )
    #glMaterialfv( GL_FRONT, GL_DIFFUSE, RED )
    #glMaterialfv( GL_FRONT, GL_AMBIENT, (0.1, 0.1, 0.1, 1.0))
    glColorMaterial( GL_FRONT, GL_AMBIENT_AND_DIFFUSE )
    glMaterialfv( GL_FRONT, GL_SPECULAR, SPEC )
    glMateriali(GL_FRONT, GL_SHININESS, 50 )
    glColor3f( 0.0,0.0,1.0 )
    glCallList( SID )
    glPopMatrix( )
     
    
# Função Principal Desenho
def draw_scene( ):
    draw_sphere( )

def display( ):
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glMatrixMode( GL_PROJECTION )
    glLoadIdentity( )
    projection( scr_size[ 0 ], scr_size[ 1 ] )
    draw_scene( )

def main():
    global ROTANGLE, SDEPTH, LIGHTS
    init_gl( scr_size[ 0 ], scr_size[ 1 ] )
    resize( scr_size[ 0 ], scr_size[ 1 ] )
    lights_setup( )

    pygame.key.set_repeat( 10, 10 )

    gen_sphere( 2, SDEPTH )
    lights_on( LIGHTS )

    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit( )
            if event.type == KEYUP and event.key == K_ESCAPE:
                sys.exit( )
            if event.type == KEYUP and event.key == K_UP:
                SDEPTH += 1
                gen_sphere( 2, SDEPTH )
            if event.type == KEYUP and event.key == K_DOWN:
                if SDEPTH > 1:
                    SDEPTH -= 1
                    gen_sphere( 2, SDEPTH )
            if event.type == KEYUP and event.key == K_l:
                LIGHTS = not LIGHTS
                lights_on( LIGHTS )
                        
        time_passed = clock.tick( )
        
        ROTANGLE += .07
        display( )        
        
        # Mostando a janela
        pygame.display.flip( )
        
if __name__ == '__main__':
    main( )
        
