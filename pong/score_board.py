from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        """Writes the latest scores on the screen"""
        self.clear()
        self.goto(x=-100, y=180)
        self.write(self.left_score, align="center", font=("Courier", 80, "bold"))
        self.goto(x=100, y=180)
        self.write(self.right_score, align="center", font=("Courier", 80, "bold"))

    def increase_left_score(self):
        """Increases the left score by 1 and writes the updated scores on the screen"""
        self.left_score += 1
        self.update()

    def increase_right_score(self):
        """Increases the right score by 1 and writes the updated scores on the screen"""
        self.right_score += 1
        self.update()
