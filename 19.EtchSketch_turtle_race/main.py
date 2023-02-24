from turtle import Turtle, Screen
import random

screen = Screen()

colors = ["blue", "green", "red", "yellow", "orange", "purple"]

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="who is going to win? Enter a color: ")


def spawn_turtles(colors_list):
    """generates the required turtles to race and positions them"""
    turtle_list = []

    offset = - 400/4
    distance =  (-offset) * 2 / len(colors_list)

    for color in colors_list:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-230, y = offset)
        offset += distance
        turtle_list.append(new_turtle)
    return turtle_list

def start_race(turtles_list):
    """moves the turtles until the end and returns the color of the winner"""
    not_finished = True
    while True:
        for turtle in turtles_list:
            turtle.forward(random.randint(10,30))
            if turtle.position()[0] >= 200:
                return turtle.color()

runners = spawn_turtles(colors)
winner = start_race(runners)
if user_bet.lower() == str(winner[0]).lower():
    print(f"you guessed it! winner was {winner}")
else:
    print(f"you got it wrong, the winner was {winner}")

screen.exitonclick()

