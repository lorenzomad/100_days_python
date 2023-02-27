from turtle import Screen
import time
import random

from player import Player
from car_manager import CarManager

# constants
WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.tracer()

player = Player()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)


screen.update()

car_manager = CarManager()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in car_manager.car_list:
        car.move() 
        if abs(car.xcor()) >= 300:
            car_manager.remove_car(car)

    if random.randint(0,100) >= 80:
        car_manager.spawn_car()


screen.exitonclick()