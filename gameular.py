import threading
import random
import os.path
from tkinter import *

widh = 500
height = 500

class Snake(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.master.title('abc')
        self.grid()

        frame1 = Frame(self)
        frame1.grid()

        self.canvas = Canvas(frame1, width=widh, height=height, bg="white")
        self.canvas.grid(columsoan = 3)
        self.canvas.focus_set()
        self.canvas.bind("<Button-1>", self.create)
        self.canvas.bind("<Key>", self.create)

        newGame = Button(frame1, text="Permainan Baru", command=self.new_game)
        newGame.grid(row=1, column=0, sticky=E)

        self.scoreLabel = Label(frame1)
        self.scoreLabel.grid(row=1, column=1)

        self.highScoreLabel = Label(frame1)
        self.highScoreLabel.grid(row=1, column=2)

        self.new_game()

    def new_game(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(widh/2, height/2-50, text="Selamat Datang di Game Ular", tag="welcome")

        rectWidth = widh/25

        rect1 = self.canvas.create_rectangle(widh/2-rectWidth/2, height, height/2+rectWidth/2, outline="black", fill= "green" ,tag="rect1")
        rect2 = self.canvas.create_rectangle(widh/2-rectWidth/2, height, height/2+rectWidth/2, outline="black", fill= "green" ,tag="rect2")
        rect3 = self.canvas.create_rectangle(widh/2-rectWidth/2, height, height/2+rectWidth/2, outline="black", fill= "green" ,tag="rect3")

        self.rectWidth = rectWidth
        self.lastDirection = None
        self.direction = None
        self.started = False
        self.game_over = False
        self.score = 0

        if (os.path.isfile("highscore.txt")) :
            scoreFile = open("highscore.txt")
            self.highScore = int(scoreFile.read())
            scoreFile.close()
        else:
            self.highScore = 0

        self.highScoreLabel["text"] = "High Score: " + str(self.highScore)

        self.rectangles = [rect1,rect2,rect3]

        self.dot = None

        self.move()
    
    def create(self, event):
        pass

    def first_movement(self):
        pass

    def _move(self):
        pass

    def move(self):
        threading.Thread(target=self._move).start()

    def make_new_dot(self):
        pass

    def grow(self):
        pass

    def check_bounds(self):
        pass

    def check_collide(self):
        frontCoords = self.canvas.coords(self.rectangles[0])

        overlapping = self.canvas.find_overlapping(frontCoords[0],frontCoords[1],frontCoords[2])

        for item in overlapping:
            if item == self.dot:
                self.grow()
                self.make_new_dot()
            if item in self.rectangles[3:]:
                self.end_game()

        #kurang kondisi ketika keluar canvas

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(widh/2, height/2, text="GAME OVER")
        if self.score > self.highScore:
            scoreFile = open("highscore.txt", "w")
            scoreFile.write(str(self.score))
            scoreFile.close()
            self.canvas.create_text(widh/2,height/2+20,text="\n Selamat! Kamu berhasil mencapai score tertinggi!")

Snake().mainloop()