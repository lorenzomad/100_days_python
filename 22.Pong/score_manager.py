from turtle import Turtle

#deefinition of constants
FONT = ("arial", 16, "normal")

class ScoreManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.left_score = 0
        self.right_score = 0
        self.write_score()
        

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.left_score} - {self.right_score}", align="center", font=FONT)

    def score_point(self, scorer):
        """updatest the score"""
        if scorer == "left":
            self.left_score += 1
        elif scorer == "right":
            self.right_score += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        if self.right_score>self.left_score:
            self.winner = "right"
        else: self.winner = "left"
        self.write(f"Game over! \nThe winner is: {self.winner}", align="center", font=FONT)
