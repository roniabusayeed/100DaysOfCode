from turtle import Turtle, Screen


# Set up the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


# Create snake body using square shaped turtles.
snake = []
SEGMENT_WIDTH = 20
for i in range(3):
    segment = Turtle(shape="square")
    segment.penup()
    segment.color("white")
    segment.setx(segment.xcor() - SEGMENT_WIDTH * i)
    snake.append(segment)

screen.exitonclick()
