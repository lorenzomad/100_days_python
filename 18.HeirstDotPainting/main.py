import random
import colorgram
import turtle as turtle_module

colors = colorgram.extract('18.HeirstDotPainting/image.jpg', 20)
rgb_colors = []
for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  rgb_colors.append((r, g, b))

# removes white colors
del rgb_colors[0:4]


def draw_dot(turtle, colors_list):
  """draw one dot at the current position"""
  color = random.choice(colors_list)
  turtle.dot(20, color)


def position_turtle(turtle, x_pos, y_pos):
  """sets the position of the turtle to x_pos and y_pos"""
  turtle.setpos(x_pos, y_pos)


tim = turtle_module.Turtle()
tim.hideturtle()
tim.penup()
turtle_module.colormode(255)
tim.speed("fastest")

distance = 50
initial_pos = -100
current_x = initial_pos
current_y_pos = initial_pos
position_turtle(tim, current_x, current_y_pos)

for _ in range(10):
  for __ in range(10):
    draw_dot(tim, rgb_colors)
    current_x += distance
    position_turtle(tim, current_x, current_y_pos)
  current_y_pos += distance
  current_x = initial_pos
  position_turtle(tim, current_x, current_y_pos)

screen = turtle_module.Screen()
screen.exitonclick()
