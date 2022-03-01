PLACEHOLDER = "[name]"

# Read invitation letter template.
with open("Input/Letters/starting_letter.txt") as letter_template_file:
    letter_template = letter_template_file.read()

# Iterate over the invited names.
with open("Input/Names/invited_names.txt") as names_file:
    for name in names_file:
        stripped_name = name.strip()  # Get rid of the trailing newlines.

        # Replace the placeholder with invited name.
        letter_content = letter_template.replace(PLACEHOLDER, stripped_name)

        # Write invitation letter to a new letter file.
        letter_filepath = f"Output/ReadyToSend/letter_for_{stripped_name}.txt"
        with open(letter_filepath, mode="w") as new_letter:
            new_letter.write(letter_content)
