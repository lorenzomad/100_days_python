from turtle import Screen
import time

from pad import Pad
from ball import Ball
#definition of costants
WIDTH = 600
HEIGHT = 600


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

left_position = - (WIDTH/2 -20) 
right_position = WIDTH/2 - 20
left_pad = Pad(left_position)
right_pad = Pad(right_position)
ball = Ball()

screen.update()

screen.listen()
screen.onkey(key="s" , fun=left_pad.move_down)
screen.onkey(key="w" , fun=left_pad.move_up)
screen.onkey(key="Down" , fun=right_pad.move_down)
screen.onkey(key="Up" , fun=right_pad.move_up)


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move_ball()
    ball.check_collision(left_pad, right_pad)
    if ball.ball_passed():
        print(f"The winner is {ball.winner}!")
        game_is_on = False

screen.exitonclick()