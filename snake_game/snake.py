from turtle import Turtle

SEGMENT_WIDTH = 20
STARTING_POSITION_X = 0

# Directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

INITIAL_SNAKE_LENGTH = 3


class Snake:
    def __init__(self):
        self.segments = []

        # Create a snake by adding segments.
        for i in range(INITIAL_SNAKE_LENGTH):
            x_pos = STARTING_POSITION_X - SEGMENT_WIDTH * i
            self.add_segment((x_pos, 0))

    @staticmethod
    def create_segment():
        """Creates a new snake segment positioned at center and returns it"""
        segment = Turtle(shape="square")
        segment.color("white")
        segment.speed("fastest")
        segment.penup()
        return segment

    def head(self):
        """Returns the head of the snake (A Turtle object)"""
        return self.segments[0]

    def move(self):
        """Moves the snake forward one step (snake.SEGMENT_WIDTH)"""

        # Make the body segments of the snake follow the ones preceding them.
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setposition(self.segments[i - 1].position())

        # Move the head one step forward.
        self.segments[0].forward(SEGMENT_WIDTH * .75)

    def add_segment(self, position):
        """"Adds a snake segment to a given position"""
        segment = self.create_segment()
        segment.setposition(position)
        self.segments.append(segment)

    def extend(self):
        """Add a new segment to the existing snake of size > 0"""
        # Add a new segment at the position of the last snake segment.
        self.add_segment(self.segments[-1].position())

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
