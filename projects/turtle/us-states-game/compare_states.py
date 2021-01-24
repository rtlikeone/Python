from turtle import Turtle


class CompareStates(Turtle):
    def __init__(self):
        super().__init__()

    def write_state_name(self, x, y, state_name):
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(f"{state_name.to_string(index=False)}")
