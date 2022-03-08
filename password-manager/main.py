import tkinter
import tkinter.messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    """Generates a random password and populates password entry"""
    pass_letters = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
    pass_digits = [random.choice(DIGITS) for _ in range(random.randint(2, 4))]
    pass_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]

    password_characters = pass_letters + pass_digits + pass_symbols
    random.shuffle(password_characters)

    password = "".join(password_characters)

    # Fill password entry with generated password.
    password_entry.delete(0, tkinter.END)  # Clear existing password from entry.
    password_entry.insert(0, password)     # Insert newly generated password.

    # Copy password to the clipboard.
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_confirmation(website, email, password):
    """Prints a message box asking user if the email and passwords are okay for the given website"""
    message = f"These are the details:\nEmail/Username: {email}\nPassword: {password}\nIs it okay to save?"
    return tkinter.messagebox.askokcancel(title=website, message=message)


def save_password():
    # Get hold of entries.
    website = website_entry.get()
    email = email_or_username_entry.get()
    password = password_entry.get()

    # Input validation.
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        tkinter.messagebox.showerror(title="Oops", message="You left some fields empty!")
        return  # No need to continue further.

    # Write entries to data file.
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    try:
        with open("data.json", "r") as data_file:
            # Load current data into memory.
            data = json.load(data_file)
            # Update data with new data.
            data.update(new_data)
    except FileNotFoundError:
        # The new data entry is the only data we've got.
        data = new_data

    with open("data.json", "w") as data_file:
        # Write updated data back into data file.
        json.dump(data, data_file, indent=4)

    # Clear entries once they are added to file.
    website_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)

    # Put focus back to website entry.
    website_entry.focus()


# ------------------------ Search password -----------------------------#
def search():
    """Searches for email and password associated with current website"""
    website = website_entry.get()

    # Load current data into memory.
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}

    # Find credentials for current website in data.
    credentials = data.get(website)
    if credentials is not None:
        email = credentials['email']
        password = credentials['password']
        tkinter.messagebox.showinfo(title=f"{website}", message=f"email: {email}\npassword: {password}")

        # Copy password to clipboard.
        pyperclip.copy(password)
    else:
        tkinter.messagebox.showinfo(title=f"{website}", message="Website not found!")


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
website_entry.config(width=35)
website_entry.grid(row=1, column=1)

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
generate_password_button.config(command=generate_password)

add_button = tkinter.Button(text="Add")
add_button.config(width=46)
add_button.grid(row=4, column=1, columnspan=2)
add_button.config(command=save_password)

search_button = tkinter.Button(text="Search")
search_button.config(width=15)
search_button.grid(row=1, column=2)
search_button.config(command=search)

window.mainloop()
