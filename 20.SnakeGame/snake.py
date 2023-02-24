import turtle



MOVE_DISTANCE = 20


class Snake():

    def __init__(self, dimension):
        self.body = []
        self.create_body(dimension)
        self.head = self.body[0]
        self.game_is_on = True

    def create_body(self, dimension):
        """creates a snake body"""
        x_pos = 0
        for _ in range(dimension):
            square = turtle.Turtle(shape="square")
            square.penup()
            square.color("white")
            square.setpos(x_pos,0)
            x_pos -= 20 
            self.body.append(square)

    def move(self, screen):
        """move the body"""
        for segment_number in range(len(self.body) - 1, 0, -1):
            new_position = self.body[segment_number - 1].position()
            self.body[segment_number].setpos(new_position)
        self.head.forward(MOVE_DISTANCE)
        

    def up(self):
        """update the direction to up"""
        if self.head.heading() != 270:
            self.head.setheading(90)
        
    def down(self):
        """update the direction to down"""
        if self.head.heading() != 90:
            self.head.setheading(270)


    def left(self):
        """update the direction to left"""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """update the direction to right"""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def game_off(self):
        """switches off the game"""
        self.game_is_on = False

    def grow(self):
        """generates a new segment"""
        new_segment = turtle.Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setpos(self.body[-1].position())
        self.body.append(new_segment)

    def collision(self):
        """detects if the snake collided with itself or with the walls"""
        wall_collision = abs(self.head.xcor()) >= 300 or abs(self.head.ycor()) >=300
        body_collision = False
        for segment in self.body[1:]:
            if self.head.pos() == segment.pos():
                body_collision = True        
        if wall_collision or body_collision:
            return True
            
