import tkinter

# Constants.
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 24, "italic")
WORD_FONT = ("Arial", 48, "bold")

# Setup UI
window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tkinter.Canvas()
canvas.config(width=800, height=526)  # Make it the same dimensions as the image.
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)  # Blend with background.
image = tkinter.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=image)  # Place the image at the center of the canvas.
canvas.create_text(400, 131, text="Title", font=TITLE_FONT)
canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)  # Place the canvas on the window.

wrong_button = tkinter.Button()
wrong_button_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button.config(image=wrong_button_image, borderwidth=0, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_button = tkinter.Button()
right_button_image = tkinter.PhotoImage(file="images/right.png")
right_button.config(image=right_button_image, borderwidth=0, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()
