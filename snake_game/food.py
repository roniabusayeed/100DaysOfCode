from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")  # Using a circular Turtle as food.
        self.penup()  # Food shouldn't draw anything.
        self.shapesize(stretch_len=.5, stretch_wid=.5)  # Food should be smaller by half the original size.
        self.color("blue")  # Food should be blue.
        self.speed("fastest")  # The turtle should show up to random position assigned asap.

        self.refresh()

    def refresh(self):
        """Relocates the food to a new random location"""
        # Put the turtle at a random position on the screen.
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setposition(x=random_x, y=random_y)
