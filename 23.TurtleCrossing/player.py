from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1.5,1.5)
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.reposition()
        self.setheading(90)
        self.game_is_on = True


    def reposition(self):
        """puts the turtle in the starting position"""
        self.goto(0, -280)
    
    def move_up(self):
        """move up"""
        if self.game_is_on:
            self.forward(20)

    def game_over(self):
        self.game_is_on =False
        