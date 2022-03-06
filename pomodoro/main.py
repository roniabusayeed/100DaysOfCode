import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text=f"Long Break", fg=RED)
        countdown(long_break_secs)
    elif reps % 2 == 0:
        timer_label.config(text=f"Short Break", fg=PINK)
        countdown(short_break_secs)
    else:
        timer_label.config(text=f"Work", fg=GREEN)
        countdown(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(seconds):
    count_min = seconds // 60  # floor division. Similar operation: math.floor(seconds / 60)
    count_sec = seconds % 60
    count_min = f"0{count_min}" if count_min < 10 else count_min
    count_sec = f"0{count_sec}" if count_sec < 10 else count_sec
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if seconds > 0:
        window.after(1000, countdown, seconds - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato timer.
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

# Timer label.
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Start button.
start = tkinter.Button(text="Start", highlightthickness=0)
start.grid(row=2, column=0)
start.config(command=start_timer)

# Reset button.
reset = tkinter.Button(text="Reset", highlightthickness=0)
reset.grid(row=2, column=2)

# Checkmark.
CHECK_MARK = "✔"
check_mark = tkinter.Label(text=CHECK_MARK, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 11, "bold"))
check_mark.grid(row=3, column=1)

window.mainloop()
