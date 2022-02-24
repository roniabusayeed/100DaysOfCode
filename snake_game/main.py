from turtle import Screen
import time
from snake import Snake
from food import Food

# Set up the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Crete a snake.
snake = Snake()

# Create food.
food = Food()

# Listen for navigation key presses.
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Move the snake.
game_is_on = True
while game_is_on:
    screen.update()  # Perform a screen update only when all the segments are moved.
    time.sleep(.05)  # The make the snake move at a reasonable speed.

    # Detect collision with food.
    if snake.head().distance(food) < 15:
        # food eaten.
        print("Nom Nom Nom!")
        # Move the food to a new place.
        food.refresh()

    snake.move()

screen.exitonclick()
