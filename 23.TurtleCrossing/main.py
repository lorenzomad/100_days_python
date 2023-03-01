from turtle import Screen
import time
import random

from player import Player
from car_manager import CarManager
from score_manager import ScoreManager

# constants
WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.tracer()

player = Player()
score = ScoreManager()

screen.listen()
screen.onkey(key="w", fun=player.move_up)


screen.update()

car_manager = CarManager()
game_is_on = True

while player.game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in car_manager.car_list:
        car.move() 
        if abs(car.xcor()) >= 300:
            car_manager.remove_car(car)
        car.detect_collision(player)
    if (random.randint(0,100) + car_manager.spawn_chance) >= 80:
        car_manager.spawn_car()
    if player.ycor() >= 280:
        player.reposition()
        car_manager.new_level()
        score.gain_point()
    
score.game_over()


screen.exitonclick()