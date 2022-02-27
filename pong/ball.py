from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        """Creates a circular ball of white color"""
        super().__init__("circle")
        self.color("white")
        self.penup()

    def move(self):
        """Increments x and y coordinates of the ball by a given amount"""
        x_offset = 5
        y_offset = 5
        self.setx(self.xcor() + x_offset)
        self.sety(self.ycor() + y_offset)
