from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, snake):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        
        self.reposition(snake)

    def reposition(self, snake):
        """move to a random position on the screen"""
        invalid = True
        while invalid:
            random_x = random.randint(-14 , 14)
            random_y = random.randint(-14, 14)
            self.goto(random_x * 20, random_y * 20)
            for segment in snake.body:
                if self.distance(segment) > 15:
                    invalid = False

    