import turtle
import time
from score_manager import ScoreManager

from snake import Snake
from food import Food

screen_width = 600
screen_height = 600

screen = turtle.Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Snake Game")

#by setting the tracer to 0 you make it work only on update method instaed of regularly
screen.tracer(0)

snake = Snake(3)
food = Food(snake)
score = ScoreManager()
screen.update()

#get inputs listening
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="c", fun=snake.game_off)

while snake.game_is_on:
    """main game loop"""
    snake.move(screen)
    if snake.head.distance(food) < 15:
        snake.grow()
        food.reposition(snake)
        score.get_points()
    if snake.collision():
        score.end_score()
        snake.game_off()
    time.sleep(0.1)
    screen.update()
screen.exitonclick()