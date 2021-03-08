import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.resizable(False, False)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Lorem ipsum, dolor sit amet",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        self.score_label = tkinter.Label(
            text=f"Score: {self.quiz.score}/{self.quiz.question_number}",
            font=("Arial", 20, "italic"),
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.grid(column=1, row=0, sticky="E")

        self.true_btn_img = tkinter.PhotoImage(file="images/true.png")
        self.true_btn = tkinter.Button(
            image=self.true_btn_img,
            command=self.true_pressed
        )
        self.true_btn.grid(column=0, row=2, sticky="W")

        self.false_btn_img = tkinter.PhotoImage(file="images/false.png")
        self.false_btn = tkinter.Button(
            image=self.false_btn_img,
            command=self.false_pressed
        )
        self.false_btn.grid(column=1, row=2, sticky="E")

        self.get_next_question()

        self.window.mainloop()

    # In a method of the 2nd class we can then tap into the method of the first class
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            # Nothing shows after the dot (self.quiz.). To have this shown, we could
            # add the datatype in the class
            # initializer above: def __init__(self, quiz_brain: )
            # We must import the specific class first (from quiz_brain import QuizBrain).
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text)
            self.score_label.config(
                text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        else:
            self.canvas.itemconfig(self.question_text, text="Game over")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        self.update_score_show_next(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.update_score_show_next(self.quiz.check_answer("False"))

    def update_score_show_next(self, check_true):
        if check_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
