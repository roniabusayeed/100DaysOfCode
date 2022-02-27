from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        """Creates a circular ball of white color"""
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Increments/Decrements x and y coordinates of the ball by an amount"""
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)

    def bounce(self):
        self.y_move *= -1  # Flip the amount by which y coordinate
        # is incremented/decremented.
