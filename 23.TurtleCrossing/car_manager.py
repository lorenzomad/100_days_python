from turtle import Turtle
import random
import time

from car import Car

class CarManager():
     
    def __init__(self) -> None:
        self.running = True
        self.car_list = []
        self.speed_offset = 0
        self.spawn_chance = 0 

    def spawn_car(self):
        """spawn 1 car on the map"""
        car_speed = random.randint(1,6) * 10 + self.speed_offset
        car_direction = random.choice([0,180])
        car_height = random.randint(-250, 250)
        
        new_car = Car(car_speed,car_direction,car_height)
        self.car_list.append(new_car)

    def remove_car(self,car):
        self.car_list.remove(car)
        car.goto(1000,1000)
        
    def remove_all(self):
        """resets all the cars"""
        for car in self.car_list:
            car.goto (1000,1000)

        self.car_list.clear()

    def new_level(self):
        self.speed_offset += 3
        self.spawn_chance += 5
        self.remove_all()

            
