import time
import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tkinter.Label(text="Score: 0/0")
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas()
        self.canvas.config(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150, 125,
            text="Hello",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280  # If width is specified, the text will be automatically wrapped.
        )

        self.true_button = tkinter.Button()
        true_button_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button.config(image=true_button_image, borderwidth=0, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.true_button.config(command=self.check_true)

        self.false_button = tkinter.Button()
        false_button_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button.config(image=false_button_image, borderwidth=0, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        self.false_button.config(command=self.check_false)

        self.get_next_question()

        self.window.mainloop()

    def give_feedback(self, is_true: bool):
        self.canvas.config(bg="green" if is_true else "red")
        self.window.after(1000, self.get_next_question)

    def check_true(self):
        is_true = self.quiz.check_answer("True")
        self.give_feedback(is_true)

    def check_false(self):
        is_true = self.quiz.check_answer("False")
        self.give_feedback(is_true)

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

        if self.quiz.still_has_questions():
            self.canvas.itemconfig(
                self.question_text,
                text=self.quiz.next_question()
            )
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
