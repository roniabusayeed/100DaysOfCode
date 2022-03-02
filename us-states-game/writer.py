from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class WriterTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def write_at_location(self, text, location):
        self.goto(location)
        self.write(text, align=ALIGNMENT, font=FONT)
