# Read invitation letter template.
with open("Input/Letters/starting_letter.txt") as letter_template_file:
    letter_template = letter_template_file.read()

# Iterate over the invited names.
with open("Input/Names/invited_names.txt") as names_file:
    for name in names_file:
        invited_name = name.strip()  # Get rid of the trailing newlines.

        # Replace the placeholder with invited name.
        letter_content = letter_template.replace("[name]", invited_name)

        # Write invitation letter to file.
        letter_filepath = f"Output/ReadyToSend/letter_for_{invited_name}.txt"
        with open(letter_filepath, "w") as invitation_letter:
            invitation_letter.write(letter_content)
