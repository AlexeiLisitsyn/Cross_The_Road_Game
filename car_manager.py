import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS = []


class CarManager:
    TIMES = 4

    def create_cars(self):
        if self.TIMES == 0:
            self.TIMES = 4
            y_cor = random.randrange(-240, 240, STARTING_MOVE_DISTANCE)
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            new_car.goto(x=290, y=y_cor)
            CARS.append(new_car)
        else:
            self.TIMES -= 1

    def detect_move(self, player):
        for car in CARS:
            if player.distance(car) < 25:
                return True
            else:
                car.forward(10)







