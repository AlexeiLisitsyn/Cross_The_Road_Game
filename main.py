import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create object and setup up key to move
player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
sec = 0.1

car_manager = CarManager()
car_manager.create_cars()

scoreboard = Scoreboard()
scoreboard.update_level()


while game_is_on:
    car_manager.create_cars()
    if car_manager.detect_move(player):
        game_is_on = False
        scoreboard.game_over()
    if player.ycor() >= 270:
        player.goto(0, -270)
        scoreboard.level_up()
        sec *= 0.6
        time.sleep(sec)
    time.sleep(sec)
    screen.update()

screen.exitonclick()
