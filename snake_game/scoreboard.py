from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
TOP_POSITION = (0, 260)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()   # Don't need to show the actual turtle. Only what it writes.
        self.penup()        # The turtle shouldn't draw anything while it moves to the top.
        self.setposition(TOP_POSITION)  # Put the turtle to the top of the screen so that it write there.
        self.color("white")  # The turtle should write in white.

        self.high_score = 0

        self.update_scoreboard()  # Display initial score (=0)

    def update_scoreboard(self):
        """"Display current score and high score at the top of the screen"""
        self.clear()  # Clear the previous score drawing from screen before drawing new score.
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """"Increases the score by 1"""
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
