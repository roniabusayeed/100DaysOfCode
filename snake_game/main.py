from turtle import Turtle, Screen
import time

# Set up the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Create snake body using square shaped turtles.
snake = []
SEGMENT_WIDTH = 20
for i in range(3):
    segment = Turtle(shape="square")
    segment.penup()
    segment.color("white")
    segment.setx(segment.xcor() - SEGMENT_WIDTH * i)
    snake.append(segment)


# Move the snake.
game_is_on = True
while game_is_on:
    screen.update()  # Perform a screen update only when all the segments are moved.
    time.sleep(.3)  # The make the snake move at a reasonable speed.

    # Make the body segments of the snake follow the ones preceding them.
    for i in range(len(snake) - 1, 0, -1):
        snake[i].setposition(snake[i-1].position())
    snake[0].forward(20)  # Move the head one step forward.


screen.exitonclick()
