from turtle import Screen
from paddle import Paddle

# Setup game screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # Turn off animation. Manually refresh screen in the game loop.

# Create paddles.
left_paddle = Paddle(x=-350, y=0)
right_paddle = Paddle(x=350, y=0)

# Make the paddles move up and down with key presses.
screen.listen()
screen.onkeypress(key="w", fun=left_paddle.up)
screen.onkeypress(key="s", fun=left_paddle.down)
screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)

# Game loop.
game_is_on = True
while game_is_on:
    screen.update()

# Exit.
screen.exitonclick()
