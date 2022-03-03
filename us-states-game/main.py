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
while len(correct_guesses) < 50:

    answer_state = screen.textinput(title=f"{len(correct_guesses)} /50 States Correct",
                                    prompt="What's another state's name? ")
    # User pressed cancel.
    if not answer_state:
        break

    # Convert answer state to title case string.
    answer_state = answer_state.title()

    if answer_state in states and answer_state not in correct_guesses:
        # Add the state to correct_guesses list if it's not already there.
        correct_guesses.append(answer_state)

        # Print state name on the image at the state's (x,y) coordinate.
        state_data = states_data[states_data.state == answer_state]
        coordinates = (int(state_data.x), int(state_data.y))
        writer.write_at_location(answer_state, coordinates)

# Find out missing states and save them to a csv file.
missing_states = [state for state in states if state not in correct_guesses]
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")

print(f"You made {len(correct_guesses)} correct guesses!")
turtle.mainloop()
