import turtle
from turtle import Turtle, Screen
import random

brush = Turtle()
brush.color("red")
brush.shape("turtle")

# Draw a dashed line.
# for _ in range(10):
#     brush.pendown()
#     brush.forward(10)
#     brush.penup()
#     brush.forward(10)


def draw_regular_polygon(n, side):
    turn_angle = 360 / n
    for _ in range(n):
        brush.forward(side)
        brush.right(turn_angle)


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
          "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# # Draw different polygons.
# for shape_side_n in range(3, 10):
#     brush.color(random.choice(colors))
#     draw_regular_polygon(shape_side_n, 100)


def random_walk(steps, pace):
    for _ in range(steps):
        brush.forward(pace)
        brush.color(random_color())
        brush.setheading(random.choice([0, 90, 180, 270]))


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(gap_angle):
    for angle in range(0, 361, gap_angle):
        brush.color(random_color())
        brush.circle(100)
        brush.setheading(angle)


brush.hideturtle()
brush.speed("fastest")
# brush.pensize(4)
turtle.colormode(255)
# random_walk(100, 30)
draw_spirograph(gap_angle=3)




screen = Screen()
screen.exitonclick()


