from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Turley")
screen.tracer(0)
screen.listen()

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "g")
screen.onkey(left_paddle.move_down, "b")

game_is_on=True

ball = Ball()

while game_is_on:
    ball.move()
    screen.update()


screen.exitonclick()
