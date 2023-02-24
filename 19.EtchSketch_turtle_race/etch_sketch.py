from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
  tim.forward(10)


def move_backward():
  tim.backward(10)


def turn_right():
  tim.right(10)


def turn_left():
  tim.left(10)


def reset_screen():
  tim.reset()


screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="c", fun=reset_screen)
screen.exitonclick()

