import turtle
import pandas
from writer import WriterTurtle

# Set up screen with map of all the states.
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # Make the image available to the turtle to use as a shape.
turtle.shape(image)  # Use image as a shape.

# Read all state's name from the csv file.
states_data = pandas.read_csv("50_states.csv")
states = states_data['state'].to_list()

# Create another turtle to write state names on the map.
writer = WriterTurtle()

correct_guesses = []  # Names of the states correctly guessed by user.

# Program loop.
should_continue = True
while should_continue:

    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name? ")
    if not answer_state:
        should_continue = False

    # Convert answer state to title case string.
    if answer_state:
        answer_state = answer_state.title()

    if answer_state in states:
        # Add the state to correct_guesses list if it's not already there.
        if answer_state not in correct_guesses:
            correct_guesses.append(answer_state)

            # Print state name on the image at the state's (x,y) coordinate.
            state_data = states_data[states_data.state == answer_state]
            coordinates = (int(state_data.x), int(state_data.y))
            writer.write_at_location(answer_state, coordinates)

    # Check if all 50 states are guessed correctly. End the game if they are.
    if len(correct_guesses) >= 50:
        should_continue = False

print(f"You made {len(correct_guesses)} correct guesses!")
turtle.mainloop()
