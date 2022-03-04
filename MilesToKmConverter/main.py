import tkinter

FONT = ("Arial", 12, "normal")

# Create window.
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=25, pady=25)

# Entry for miles.
entry = tkinter.Entry()
entry.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

is_equal_to_label = tkinter.Label(text="is equal to", font=FONT)
is_equal_to_label.grid(row=1, column=0)

result_label = tkinter.Label(text="0", font=FONT)
result_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)


# Calculate button event handler.
def calculate():
    miles = float(entry.get())
    km = round(miles * 1.60934, 2)
    result_label.config(text=f"{km}")


# calculate.
calculate_button = tkinter.Button(text="Calculate")
calculate_button.grid(row=2, column=1)
calculate_button.config(command=calculate)


window.mainloop()
