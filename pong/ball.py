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

    def bounce_y(self):
        """Bounce the ball vertically"""
        self.y_move *= -1  # Flip the amount by which y coordinate
        # is incremented/decremented.

    def bounce_x(self):
        """Bounce the ball horizontally"""
        self.x_move *= -1  # Flip the amount by which x coordinate
        # is incremented/decremented.

    def refresh(self, right=True):
        """Re-centers the ball and sets the direction towards right(by default) or left
         if right=False"""
        self.goto(0, 0)
        if right:
            self.x_move = abs(self.x_move)
        else:
            self.x_move = -abs(self.x_move)
        self.y_move = abs(self.y_move)
