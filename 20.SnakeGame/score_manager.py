from turtle import Turtle

FONT =("arial", 16, "normal") 
GAME_OVER_FONT = ("arial", 24, "bold")
ALIGNMENT = "center"

class ScoreManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.setposition(0, 270)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.initialize_high_score()
        self.write_score()
        
    def initialize_high_score(self):
        with open("high_score.txt") as data:
            self.high_score = int(data.read()) 

    def save_high_score(self, new_score):
        """writes to file the new high score"""
        with open("high_score.txt", 'w') as data:
            data.write(str(self.score))

    def write_score(self):
        """writes the score to the screen"""
        self.clear()
        self.write(f"Score: {self.score}. High score: {self.high_score}", align= ALIGNMENT, font=FONT)

    def get_points(self):
        """adds the points to the score"""
        self.score += 10
        self.write_score()

    def end_score(self):
        """shows the end value"""
        self.goto(0, 0)
        self.write(f"Game over! \nYour score was: {self.score}", align= ALIGNMENT, font=GAME_OVER_FONT)
        if self.score > self.high_score:
            self.save_high_score(self.score)
