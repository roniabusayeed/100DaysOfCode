import turtle
from turtle import Turtle, Screen
import colorgram
import random


# Extract rgb colors from image.
colors = colorgram.extract("image.jpg", 20)
threshold = 0.7  # Assuming background color will occupy more than 70%
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors if color.proportion < threshold]

# Configure our turtle.
turtle.colormode(255)
brush = Turtle()
brush.speed("fastest")
brush.hideturtle()
brush.penup()


# Configure our paint.
HORIZONTAL_DOTS = 10
VERTICAL_DOTS = 10
DOT_SIZE = 20
PACE = 50
x_offset = -220
y_offset = -200

# Draw the paining.
for row in range(HORIZONTAL_DOTS):
    brush.sety(row * PACE + y_offset)
    for column in range(VERTICAL_DOTS):
        brush.setx(column * PACE + x_offset)
        brush.dot(DOT_SIZE, random.choice(rgb_colors))


# Wait for click to exit.
screen = Screen()
screen.exitonclick()
