import tkinter

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.resizable(False, False)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Lorem ipsum, dolor sit amet", font=("Arial", 20, "italic"))
        self.canvas.grid(column=1, columnspan=2, row=1)

        self.score_label = tkinter.Label(text="Score:", font=("Arial", 20, "italic"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=2, row=0, sticky="E")

        self.true_btn_img = tkinter.PhotoImage(file="images/true.png")
        self.true_btn = tkinter.Button(image=self.true_btn_img)
        self.true_btn.grid(column=1, row=3, sticky="W")

        self.false_btn_img = tkinter.PhotoImage(file="images/false.png")
        self.false_btn = tkinter.Button(image=self.false_btn_img)
        self.false_btn.grid(column=2, row=3, sticky="E")


        self.window.mainloop()
