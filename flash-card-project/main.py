import tkinter
import pandas
import random


# Constants.
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# Load words/translation from file.
data = pandas.read_csv("data/french_words.csv")
# dictionary = [{"French": row.French, "English": row.English} for _, row in data.iterrows()]
dictionary = data.to_dict(orient="records")  # Achieves the same thing with DataFrame.to_dict(orient='records')


def next_card():
    """Generates a new random French word/translation and populates the flashcard"""
    # Pick a random word/translation from dictionary.
    word_translation_pair = random.choice(dictionary)

    # Populate the flashcard.
    french_word = word_translation_pair["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=french_word)


# Setup UI
window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tkinter.Canvas()
canvas.config(width=800, height=526)  # Make it the same dimensions as the image.
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)  # Blend with background.
image = tkinter.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=image)  # Place the image at the center of the canvas.
card_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)  # Place the canvas on the window.

wrong_button = tkinter.Button()
wrong_button_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button.config(image=wrong_button_image, borderwidth=0, highlightthickness=0)
wrong_button.grid(row=1, column=0)
wrong_button.config(command=next_card)

right_button = tkinter.Button()
right_button_image = tkinter.PhotoImage(file="images/right.png")
right_button.config(image=right_button_image, borderwidth=0, highlightthickness=0)
right_button.grid(row=1, column=1)
right_button.config(command=next_card)

# Display the first card upon startup.
next_card()

window.mainloop()
