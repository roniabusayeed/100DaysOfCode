from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto_start()

    def move(self):
        """Moves the player vertically upward by player.MOVE_DISTANCE"""
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        """Returns True if player has crossed the finish line. Returns False otherwise"""
        return self.ycor() >= FINISH_LINE_Y

    def goto_start(self):
        """Takes the player back to starting position: The bottom of the screen"""
        self.goto(STARTING_POSITION)
