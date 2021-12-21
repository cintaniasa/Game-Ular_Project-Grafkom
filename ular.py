from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
from math import*

def rasiocanvas(): 
    glClearColor(0.0,0.8,0.9,1.0) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-4,12,-4,12) 
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def Circle_polygon(x_pos, y_pos, radius, sides):          
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + x_pos  
        sine  = radius * sin(i*2*pi/sides) + y_pos   
        glVertex2f(cosine,sine) 

def lingkaran_c(x,y):
    glColor3ub(255, 102, 227)
    Circle_polygon(x,y,50.00,100.00)
    glEnd()

def lingkaran_d(x,y):
    glColor3f(0,0,0)
    Circle_polygon(x -18.00,y+ 4.00,10.00,100.00)
    glEnd()

def lingkaran_f(x,y):
    glColor3f(0,0,0)
    Circle_polygon(x+ 18.00,y+ 4.00,10.00,100.00)
    glEnd()

def lingkaran_g(x,y):
    glColor3f(0,0,0)
    Circle_polygon(x -8.00,y+ -15.00,10.00,100.00)
    glEnd()

def lingkaran_h(x,y):
    glColor3f(0,0,0)
    Circle_polygon(x+ 8.00,y+ -15.00,10.00,100.00)
    glEnd()

def gabung(x,y):
    lingkaran_c(x,y)
    lingkaran_d(x,y)
    lingkaran_f(x,y)
    lingkaran_g(x,y)
    lingkaran_h(x,y)
