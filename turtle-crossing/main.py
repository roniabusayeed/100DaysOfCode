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

# Create car manager.
car_manager = CarManager()

# Create the scoreboard.
scoreboard = Scoreboard()

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

    # Detect collision with cars. Stop the game if collided.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()  # Display game over message.

    # Detect if player has reached the finish line.
    if player.at_finish_line():
        # Take the player back to starting position for next level.
        player.goto_start()

        # Speed up the cars because the player is at the next level.
        car_manager.level_up()

        # Update level/score.
        scoreboard.level_up()
        scoreboard.update_scoreboard()


screen.exitonclick()
