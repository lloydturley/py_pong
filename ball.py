from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        #self.speed("fastest")
        time.sleep(.1)
        self.goto(self.xcor() + 10, self.ycor() + 10)

