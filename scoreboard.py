from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score=0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-100,200)
        self.write_score()


    def increment_leftscore(self):
        self.left_score+=1
        self.write_score()

    def increment_rightscore(self):
        self.right_score += 1
        self.write_score()

    def write_score(self):
        print(f"left is {self.left_score}.  right is {self.right_score}")
        self.clear()
        self.write(f"left is {self.left_score}.  right is {self.right_score}")

