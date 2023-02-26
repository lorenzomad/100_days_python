from turtle import Turtle

#definition of costants
DIMENSION = 3
MOVE_DISTANCE = 40
UP = 90
DOWN = 270


class Pad():
    def __init__(self, starting_pos):

        self.create_pad(starting_pos)

    def create_pad(self, starting_x):
        """generates the body of the pad"""
        self.pad_segments = []
        starting_y = DIMENSION * 20 - 2
        for _ in range (DIMENSION):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(starting_x, starting_y) 
            starting_y -= 20
            self.pad_segments.append(segment)

    def move_up(self):
        """move all the elements of the distance"""
        for segment in self.pad_segments:
            segment.setheading(UP)
            segment.forward(MOVE_DISTANCE)

    def move_down(self):
        """move all the elements of the distance"""
        for segment in self.pad_segments:
            segment.setheading(DOWN)
            segment.forward(MOVE_DISTANCE)

