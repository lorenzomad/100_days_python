from turtle import Turtle

class Car(Turtle):
    def __init__(self, car_speed, direction, height) -> None:
        super().__init__()
        self.shape("square")
        self.car_speed = car_speed
        self.speed("fastest")
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