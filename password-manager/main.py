import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Setup window.
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Setup logo.
canvas = tkinter.Canvas(height=200, width=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Setup input labels.
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

email_or_username_label = tkinter.Label(text="Email/Username:")
email_or_username_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# Setup input text fields and buttons.
website_entry = tkinter.Entry()
website_entry.config(width=55)
website_entry.grid(row=1, column=1, columnspan=2)

# Make website entry in focus.
website_entry.focus()

email_or_username_entry = tkinter.Entry()
email_or_username_entry.config(width=55)
email_or_username_entry.grid(row=2, column=1, columnspan=2)

# Pre-populate email field.
email_or_username_entry.insert(tkinter.END, "roni.abusayeed@gmail.com")

password_entry = tkinter.Entry()
password_entry.config(width=35)
password_entry.grid(row=3, column=1)

generate_password_button = tkinter.Button(text="Generate Password")
generate_password_button.config(width=15)
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add")
add_button.config(width=46)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
