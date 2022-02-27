from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Setup game screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # Turn off animation. Manually refresh screen in the game loop.

# Create paddles.
left_paddle = Paddle(x=-350, y=0)
right_paddle = Paddle(x=350, y=0)

# Create the ball.
ball = Ball()

# Make the paddles move up and down with key presses.
screen.listen()
screen.onkeypress(key="w", fun=left_paddle.up)
screen.onkeypress(key="s", fun=left_paddle.down)
screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)

# Game loop.
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    # Detect collision with the ceiling and the floor.
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce_y()

    # Detect collision with the paddles.
    right_wall = right_paddle.xcor() - 10
    left_wall = left_paddle.xcor() + 10
    threshold = 50
    if ball.distance(right_paddle) < threshold and ball.xcor() > right_wall \
            or ball.distance(left_paddle) < threshold and ball.xcor() < left_wall:
        ball.bounce_x()

    ball.move()

# Exit.
screen.exitonclick()
