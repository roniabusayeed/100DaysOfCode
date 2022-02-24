from turtle import Turtle

SEGMENT_WIDTH = 20
STARTING_POSITION_X = 0

# Directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.setx(STARTING_POSITION_X - SEGMENT_WIDTH * i)
            self.segments.append(segment)

    def move(self):
        """Moves the snake forward one step (snake.SEGMENT_WIDTH)"""

        # Make the body segments of the snake follow the ones preceding them.
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setposition(self.segments[i - 1].position())

        # Move the head one step forward.
        self.segments[0].forward(SEGMENT_WIDTH)

    def up(self):
        if not self.segments[0].heading() == DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if not self.segments[0].heading() == UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if not self.segments[0].heading() == RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if not self.segments[0].heading() == LEFT:
            self.segments[0].setheading(RIGHT)
