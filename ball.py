from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self, direction):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_y = 10
        if direction=="right" or direction=="":
            self.move_x = 10
        else:
            self.move_x = -10

    def move(self, collision):
        if collision == "wall":
            self.move_y = -self.move_y
        elif collision == "paddle":
            self.move_x = -self.move_x
        time.sleep(.1)
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)
