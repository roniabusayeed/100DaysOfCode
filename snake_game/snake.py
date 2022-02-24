from turtle import Turtle

SEGMENT_WIDTH = 20
STARTING_POSITION_X = 0


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
        # Make the body segments of the snake follow the ones preceding them.
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setposition(self.segments[i - 1].position())
        self.segments[0].forward(SEGMENT_WIDTH)  # Move the head one step forward.

    def up(self):
        if not self.segments[0].heading() == 270:
            self.segments[0].setheading(90)

    def down(self):
        if not self.segments[0].heading() == 90:
            self.segments[0].setheading(270)

    def left(self):
        if not self.segments[0].heading() == 0:
            self.segments[0].setheading(180)

    def right(self):
        if not self.segments[0].heading() == 180:
            self.segments[0].setheading(0)
