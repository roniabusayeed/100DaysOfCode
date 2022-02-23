from turtle import Turtle, Screen
import random


# Setup screen.
screen = Screen()
screen.setup(width=500, height=400)

# Remember user bet.
user_bet = screen.textinput(title="Make a Bet", prompt="Which turtle is going to win the race? Enter a color: ")


def get_race_turtle(x, y, color):
    """Returns a race turtle at position (x, y) with given color.
    A race turtle doesn't draw anything as it moves"""
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.penup()
    turtle.color(color)
    turtle.setposition(x=x, y=y)
    return turtle


# Generate same number of race turtles as there are colors with a uniform vertical spacing.
turtle_colors = ["red", "green", "blue", "yellow", "purple"]
race_turtles = []
VERTICAL_SPACING = 50
STARTING_LINE = -230
for i in range(len(turtle_colors)):
    vertical_position = VERTICAL_SPACING * (i - len(turtle_colors) / 2)
    race_turtles.append(get_race_turtle(x=STARTING_LINE, y=vertical_position, color=turtle_colors[i]))


def get_winner(turtles, finish_line_xcor):
    """Returns the first occurrence of the turtle that crossed the finish line.
    Returns None in case no turtle crossed finish line."""
    for turtle in turtles:
        if turtle.xcor() >= finish_line_xcor:
            return turtle


def advance(turtles, max_pace):
    """"Moves all the turtles to the right/forward with a random pace between [0,max_pace)"""
    for turtle in turtles:
        turtle.forward(random.random() * max_pace)


# Make the turtles race against each other.
FINISH_LINE_XCOR = screen.window_width() / 2
MAX_PACE = 10
race_should_continue = True
while race_should_continue:
    winner = get_winner(race_turtles, FINISH_LINE_XCOR)
    if winner:
        print(f"Winner is {winner.pencolor()} turtle!")
        if winner.pencolor() == user_bet:
            print("You win!")
        else:
            print("You lose!")
        race_should_continue = False
    else:
        advance(race_turtles, MAX_PACE)


# Wait for the user to click to exit window.
screen.exitonclick()
