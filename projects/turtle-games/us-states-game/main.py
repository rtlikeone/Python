import turtle
import pandas
from compare_states import CompareStates
from score import Score

screen = turtle.Screen()
screen.title("U.S. States Game")

# Add new shape and make it available to use as a shape below
image = "blank_states_img.gif"
screen.addshape(image)
# Use newly added shape as an image
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

state_name = CompareStates()
score = Score()

guessed = []

while len(guessed) < 50:

    # Show pop-up box and get user input
    answer_state = screen.textinput(title=f"{score.score}/50 States Correct", prompt="What's another state's name?").title()

    compare_user_input = data[data.state == answer_state]

    if answer_state == "Exit":
        # states_to_learn = []
        # for value in all_states:
        #     if value not in guessed:
        #         states_to_learn.append(value)

        # Conditional list comprehension. The above can be refactored like this:
        states_to_learn = [state for state in all_states if state not in guessed]

        print(states_to_learn)
        states_to_csv = pandas.DataFrame(states_to_learn)
        states_to_csv.to_csv("states_to_learn.csv")
        break


    if len(compare_user_input):
        state = compare_user_input.state
        x = int(compare_user_input.x)
        y = int(compare_user_input.y)
        state_name.write_state_name(x, y, state)
        guessed.append(state.to_string(index=False))
        score.update_score()
    else:
        print("Please type a correct State's name")

# turtle.mainloop()
