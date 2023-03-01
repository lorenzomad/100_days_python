from turtle import Turtle
import random

COLORS = [  "blue", "yellow", "red", "green", "purple", "black", "orange"]
class Car(Turtle):
    def __init__(self, car_speed, direction, height) -> None:
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.color(random.choice(COLORS))
        self.car_speed = car_speed
        self.penup()
        if direction == 0:
            x_position = -300
        else:
            x_position = 300
        self.goto(x_position, height)
        self.setheading(direction)
        self.shapesize(1,2)


    def move(self):
        """moves the car forward"""
        self.forward(self.car_speed)

    def detect_collision(self, player):
        """detects collisions with the player and game over in case it does"""
        if self.distance(player) <=30:
            player.game_over()