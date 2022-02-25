from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()   # Don't need to show the actual turtle. Only what it writes.
        self.penup()        # The turtle shouldn't draw anything while it moves to the top.
        self.setposition(x=0, y=260)  # Put the turtle to the top of the screen so that it write there.
        self.color("white")  # The turtle should write in white.

        self.display()  # Display initial score (=0)

    def display(self):
        self.clear()  # Clear the previous score drawing from screen before drawing new score.
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

