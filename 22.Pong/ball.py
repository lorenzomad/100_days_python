from turtle import Turtle
import random

#definition of constants
LEFT = 0
RIGHT = 1
UP = 0
DOWN = 1
#balldirections
UPRIGHT = 45
UPLEFT = 45 + 90
DOWNLEFT = 45 + 90*2
DOWNRIGHT = 45 + 90*3

class Ball(Turtle):
    def __init__(self) :
        super().__init__(shape = "circle")
        self.color("white")
        self.penup()
        self.generate_ball()
        self.game_is_on = True


    def generate_ball(self):
        """generates the ball"""
        #direction 0 =left 1 = right
        self.move_distance = 3
        self.goto(0,0)
        self.direction_x = random.randint(0,1)
        self.direction_y = random.randint(0,1)
        self.change_direction()

    def change_direction(self):
        """updates the direction of the ball"""
        if self.direction_x == LEFT:
            if self.direction_y == DOWN:
                self.setheading(DOWNLEFT)
            elif self.direction_y == UP:
                self.setheading(UPLEFT)
        elif self.direction_x == RIGHT:
            if self.direction_y == DOWN:
                self.setheading(DOWNRIGHT)
            elif self.direction_y == UP:
                self.setheading(UPRIGHT)

    def move_ball(self):
        """updates the position of the ball and checks the collisions 
        with walls """
        self.forward(self.move_distance)
        if self.ycor() >= 300:
            self.direction_y = DOWN
            self.change_direction()
        elif self.ycor() <= - 300:
            self.direction_y = UP
            self.change_direction()

    def check_collision(self, left_pad, right_pad):
        """check the collision with left and right pads 
        (order of inputs matters)"""
        for segment in left_pad.pad_segments:
            if self.distance(segment) <=15:
                self.direction_x = RIGHT
                self.change_direction()
                self.move_distance += 1
                break
        for segment in right_pad.pad_segments:
            if self.distance(segment) <=15:
                self.direction_x = LEFT
                self.change_direction()
                self.move_distance += 1
                break

    def ball_passed(self):
        """checks the win condition and returns the winner"""
        if self.xcor() <= -400:
            self.winner = "right"
            return True
        elif self.xcor() >= 400:
            self.winner = "left"
            return True
        return False
    
    def game_off(self):
        self.game_is_on = False





