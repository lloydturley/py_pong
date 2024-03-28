from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = Screen()
screen.bgcolor("black")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Pong Turley")
screen.tracer(0)
screen.listen()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "g")
screen.onkey(left_paddle.move_down, "b")

start_direction = "right"
scoreboard = Scoreboard()

while True:
    ball = Ball(start_direction)
    game_is_on = True
    while game_is_on:
        if ball.ycor() > (SCREEN_HEIGHT / 2) - 25 or ball.ycor() < -((SCREEN_HEIGHT / 2) - 25):
            ball.move("wall")
        elif ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(
                left_paddle) < 50 and ball.xcor() < -320:
            ball.move("paddle")
        elif ball.xcor() > 321:
            print("Left scored!")
            ball.hideturtle()
            game_is_on = False
            start_direction = "left"
            scoreboard.increment_leftscore()
        elif ball.xcor() < -321:
            print("Right scored!")
            ball.hideturtle()
            game_is_on = False
            start_direction = "right"
            scoreboard.increment_rightscore()
        else:
            ball.move("")
        screen.update()

screen.exitonclick()
