from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(x=-250, y=250)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update screen with current level"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        """Increments the level by 1"""
        self.level += 1

    def game_over(self):
        """Prints the 'Game Over' message at the center of the screen"""
        self.goto((0, 0))
        self.write("Game Over", align="center", font=FONT)
