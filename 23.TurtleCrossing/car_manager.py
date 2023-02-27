from turtle import Turtle
import random
import time

from car import Car

class CarManager():
     
    def __init__(self) -> None:
        self.running = True
        self.car_list = []


    def spawn_car(self):
        """spawn 1 car on the map"""
        car_speed = random.randint(1,6) * 10
        car_direction = random.choice([0,180])
        car_height = random.randint(-250, 250)
        
        new_car = Car(car_speed,car_direction,car_height)
        self.car_list.append(new_car)

    def remove_car(self,car):
        self.car_list.remove(car)
        


            
