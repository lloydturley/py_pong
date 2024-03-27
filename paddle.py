from turtle import Turtle

PADDLE_SPEED = "fastest"
SHAPE = "square"
SHAPE_WIDTH = 5
SHAPE_HEIGHT = 1


class Paddle(Turtle):

    def __init__(self, starting_location):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.color("white")
        self.shapesize(SHAPE_WIDTH, SHAPE_HEIGHT)
        self.speed("fastest")
        self.goto(starting_location)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
