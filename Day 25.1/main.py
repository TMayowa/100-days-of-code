import turtle
from state import State
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
state = State()
guess_right = []

df = pd.read_csv("50_states.csv")
states_list = df["state"].to_list()
print(states_list)


while len(guess_right) < 50:
    answer_state_raw = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name")
    answer_state = answer_state_raw.title()

    if answer_state == 'Exit':
        break
    #CHECKING AND UPDATING GUESS
    if answer_state in states_list:
        score += 1
        guess_right.append(answer_state)
        state.create_state()
        location = df[df.state == answer_state]
        print(location.x, location.y)
        state.goto(int(location.x), int(location.y))
        state.write(f"{answer_state}", True, align = 'center', font= ("Arial", 8, "normal"))

states_to_learn = list(set(states_list).difference(guess_right))
dataframe = pd.DataFrame(states_to_learn, columns=['states'])
dataframe.to_csv('states_to_learn.csv')
