from turtle import Turtle, Screen
import time
from snake import Snake

# Set up the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Crete a snake.
snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Move the snake.
game_is_on = True
while game_is_on:
    screen.update()  # Perform a screen update only when all the segments are moved.
    time.sleep(.3)  # The make the snake move at a reasonable speed.

    snake.move()

screen.exitonclick()
