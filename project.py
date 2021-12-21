from math import trunc
from os import stat
import OpenGL.GL
import OpenGL.GLUT 
import OpenGL.GLU
import ular
import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

posisi_ular=[0,0]
speed=15
gerakAtas=True
gerakBawah=True
gerakKiri=True
gerakKanan=True

state='start'
food = None
score = 0

# Fungsi menggunakan objek kotak
def bentuk():

    glBegin(GL_QUADS) 
    glColor3ub(87, 97, 212)
    glVertex2f(-400, 400) #a
    glVertex2f(-400, -400) #b
    glVertex2f(-350, -400) #e
    glVertex2f(-350, 400) #f
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(87, 97, 212)
    glVertex2f(-400, 400) #a
    glVertex2f(400, 400) #d
    glVertex2f(400, 350) #h
    glVertex2f(-400, 350) #f
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(87, 97, 212)
    glVertex2f(350, 400) #i
    glVertex2f(400, 400) #d
    glVertex2f(400, -400) #c
    glVertex2f(350, -400) #j
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(87, 97, 212)
    glVertex2f(400, -350) #k
    glVertex2f(400, -400) #c
    glVertex2f(-400, -400) #b
    glVertex2f(-400, -350) #l
    glEnd()

# Fungsi untuk mengkonfigurasi tulisan yang berada pada akhir stage atau tiap level
def game_over(atas,bawah,kiri,kanan):
    global state
    if ((posisi_ular[0]<=kanan and posisi_ular[0] >=kiri) and (posisi_ular[1] <=atas and posisi_ular[1] >=bawah)):
        state='gameover'

 # Random makanan ular (tantangan)
def makanan(x,y):
    glBegin(GL_QUADS) 
    glColor3ub(237, 240, 245)
    glVertex2f(x,y) #a
    glVertex2f(x,y-10) #b
    glVertex2f(x-10,y-10) #c
    glVertex2f(x-10,y) #d
    glEnd()

def make_new_dot(food):
    global posisi_ular
    global score
    if food != None:
        food = None
    dotX = random.randint(-100,100)
    dotY = random.randint(-100,100)
    food = makanan(dotX,dotY)
    if ((posisi_ular[0]>=dotX-10 and posisi_ular[0]<=dotX) and (posisi_ular[1] <=dotY and posisi_ular[1] >=dotY-10)):
        score += 10
        make_new_dot(food)
    
# Fungsi Iterasi    
def iterate():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-800/2,800/2,-800/2,800/2)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

#Fungsi mengkonfigurasi Tulisan
def drawText(text,x,y, R, G, B): 
    glPushMatrix()
    glColor3ub(R, G, B)
    glRasterPos2i(x, y)
    for i in str(text):
        c = ord(i)
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, c)
    glPopMatrix()

# Fungsi memunculkan suatu object di sebuah layar 
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Untuk membersihkan layar
    glLoadIdentity() # Untuk mereset semua posisi grafik/bentuk
    iterate() # Fungsi lopping
    if state=='start':
        ular.gabung(posisi_ular[0],posisi_ular[1])
        bentuk()
        drawText('SCORE : '+ score, -80,-300,255,0,255)
        make_new_dot(food)
        game_over(400,-400,-400,-310)
        game_over(400,310,-400,400)
        game_over(400,-400,310,400)
        game_over(-310,-400,-400,400)
    elif state=='gameover':
        drawText('GAME OVER !!',-100,0,255, 0,0)
        drawText('Thanks You',-80,-300,21, 255, 0)
    
    glutSwapBuffers() # Untuk membersihkan layar

# Mengatur mengontrol Gerakan    
def controller(key,x,y): 
    global gerakKanan
    global gerakKiri
    global gerakBawah
    global gerakAtas
    if key==GLUT_KEY_UP and gerakAtas:
        if gerakBawah==False:
            gerakBawah=True
        posisi_ular[1]+=speed
    if key==GLUT_KEY_DOWN and gerakBawah:
        if gerakAtas==False:
            gerakAtas=True
        posisi_ular[1]-=speed
    if key==GLUT_KEY_LEFT and gerakKiri:
        if gerakKanan==False:
            gerakKanan=True
        posisi_ular[0]-=speed
    if key==GLUT_KEY_RIGHT and gerakKanan:
        if gerakKiri==False:
            gerakKiri=True
        posisi_ular[0]+=speed

# Inisialisasi
glutInit() # inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) # Untuk mengatur layar menjadi berwarna
glutInitWindowSize(800, 800)  # Untuk mengatur ukuran layar/window
glutInitWindowPosition(0, 0) # Untuk mengatur posisi window
wind = glutCreateWindow("Snake Game") # Memberi nama pada window
glutDisplayFunc(showScreen) # Untuk menampilkan objek pada layar, fungsi callback
glutSpecialFunc(controller) # Untuk mengaktifkan Kontrol
glutIdleFunc(showScreen) # Untuk menyuruh OpenGL untuk selalu membuka dan menampilkan objek
glutMainLoop() # Untuk memulai segalanya, untuk me-looping Objek
