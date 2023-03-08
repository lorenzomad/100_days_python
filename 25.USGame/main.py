import turtle
import pandas as pd

image = "blank_states_img.gif"
location_file = "50_states.csv"

states_location = pd.read_csv(location_file)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.color("black")


def get_answer():
    return screen.textinput(f"{len(guessed_states) }/50 States Guessed", "What is the name of a state").title()

def write_state(correct_answer, x, y):
    writer.goto(x, y)
    writer.write(correct_answer, font = ("arial", 8, "normal"))
    

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)

turtle.shape(image)

guessed_states = []

while(len(guessed_states) <= 50 and guessed_states != ""):
    answer_state = get_answer()
    
    if answer_state == None:
        break
    elif answer_state in states_location["state"].values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state = states_location[states_location["state"] == answer_state]
        x_pos = int(state.x)
        y_pos = int(state.y)
        write_state(answer_state, x_pos, y_pos)


turtle.mainloop()

