from turtle import Turtle

FONT = ("Arial", 16, "normal")

class ScoreManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.score = 0
        self.goto(0,270)
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align= "center", font= FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER. \n The final score is {self.score}", align= "center", font=FONT)

    def gain_point(self):
        self.score += 1
        self.write_score()