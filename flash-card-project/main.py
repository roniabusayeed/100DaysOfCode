import tkinter
import pandas
import random


# Constants.
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# Load words/translation from file.

# If there is a progress file (of fewer words) saved, load it;
# otherwise, load the full list.
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

# dictionary = [{"French": row.French, "English": row.English} for _, row in data.iterrows()]
# Achieves the same thing with DataFrame.to_dict(orient='records')
dictionary = data.to_dict(orient="records")

# Keep track of the previously scheduled delayed execution of flip card operation.
previous_after_id = None

# Keep track of current word/translation pair.
current_word = None


def is_known():
    """Removes the current word from loaded dictionary so that it doesn't show up again"""
    dictionary.remove(current_word)

    # Save current dictionary.
    pandas.DataFrame(dictionary).to_csv("data/words_to_learn.csv", index=False)


def next_card():
    """Generates a new random French word/translation and populates the flashcard"""
    global previous_after_id
    global current_word
    # Pick a random word/translation from dictionary.
    current_word = random.choice(dictionary)

    # Populate the flashcard.
    canvas.itemconfig(image, image=front_image)
    french_word = current_word["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")

    # Invalidate previously scheduled delayed execution of flip card.
    if previous_after_id is not None:
        window.after_cancel(previous_after_id)

    # Flip the card after some delay.
    delay_in_ms = 3000  # the card should flip after 3 seconds.
    previous_after_id = window.after(delay_in_ms, flip_card)


def flip_card():
    """Flips the card with a new image and English translation (parameter)"""
    canvas.itemconfig(image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")


# Setup UI
window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tkinter.Canvas()
canvas.config(width=800, height=526)  # Make it the same dimensions as the image.
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)  # Blend with background.
front_image = tkinter.PhotoImage(file="images/card_front.png")
image = canvas.create_image(400, 263, image=front_image)  # Place the image at the center of the canvas.
card_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)  # Place the canvas on the window.

# Used when the card is flipped.
back_image = tkinter.PhotoImage(file="images/card_back.png")


wrong_button = tkinter.Button()
wrong_button_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button.config(image=wrong_button_image, borderwidth=0, highlightthickness=0)
wrong_button.grid(row=1, column=0)
wrong_button.config(command=next_card)

right_button = tkinter.Button()
right_button_image = tkinter.PhotoImage(file="images/right.png")
right_button.config(image=right_button_image, borderwidth=0, highlightthickness=0)
right_button.grid(row=1, column=1)
right_button.config(command=lambda: [is_known(), next_card()])

# Display the first card upon startup.
next_card()

# Keep window visible.
window.mainloop()
