from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x: int, y: int):
        """Creates a paddle at a given position on the screen"""
        super().__init__()
        self.setposition(x=x, y=y)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")

    def up(self):
        """Moves the paddle vertically upward"""
        self.sety(self.ycor() + 20)

    def down(self):
        """Moves the paddle vertically downward"""
        self.sety(self.ycor() - 20)
