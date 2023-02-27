from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1.5,1.5)
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.goto(0, -280)
        self.setheading(90)

    def move_up(self):
        """move up"""
        self.forward(10)

        