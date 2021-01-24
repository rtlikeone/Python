import turtle
import pandas
from write_state_name import WriteStateName
from score import Score

screen = turtle.Screen()
screen.title("U.S. States Game")

# Add new shape and make it available to use as a shape below
image = "blank_states_img.gif"
screen.addshape(image)
# Use newly added shape as an image
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_name = WriteStateName()
score = Score()

game_on = True
guessed = []

while game_on:
    if len(guessed) == 49:
        print("You've guessed them All.")
        break

    # Show pop-up box and get user input
    answer_state = screen.textinput(title=f"{score.score}/50 States Correct", prompt="What's another state's name?").title()

    compare_user_input = data[data.state == answer_state]

    if len(compare_user_input):
        state = compare_user_input.state
        x = int(compare_user_input.x)
        y = int(compare_user_input.y)
        state_name.write_state_name(x, y, state)
        guessed.append(state.to_string(index=False))
        score.update_score()
    else:
        print("Please type a correct State's name")

turtle.mainloop()
