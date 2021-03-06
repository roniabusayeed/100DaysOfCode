from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


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


# Keep track of score.
score_board = ScoreBoard()

# Move the snake.
game_is_on = True
while game_is_on:
    screen.update()  # Perform a screen update only when all the segments are moved.
    time.sleep(.1)  # Make the snake move at a reasonable speed.

    # Detect collision with food.
    if snake.head().distance(food) < 15:
        # Move the food to a new place.
        food.refresh()

        # Update score.
        score_board.increase_score()
        score_board.update_scoreboard()

        # Increase size of the snake by one segment.
        snake.extend()

    # Detect collision with the wall.
    if snake.head().xcor() > 280 or snake.head().xcor() < -280 or\
            snake.head().ycor() > 280 or snake.head().ycor() < -280:
        # game_is_on = False
        snake.reset()
        score_board.reset()

    # Detect collision with tail.
    # If the head collides with any segment in the tail (essentially, rest of the snake),
    # trigger game over sequence.
    for segment in snake.segments[1:]:
        if snake.head().distance(segment) < 10:
            # game_is_on = False
            snake.reset()
            score_board.reset()

    snake.move()


screen.exitonclick()
