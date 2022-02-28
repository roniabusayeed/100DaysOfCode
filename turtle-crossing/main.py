import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player.
player = Player()
car_manager = CarManager()

# Move the player forward upon pressing the 'up' key.
screen.listen()
screen.onkeypress(key="Up", fun=player.move)

# Game loop.
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Probably create a new car.
    car_manager.create_car()

    # Move all the generated cars.
    car_manager.move_cars()
