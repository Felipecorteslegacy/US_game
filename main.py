import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. game trivia")
image = "blank_states_img.gif"
screen.setup(width=725, height=491)
screen.addshape(image)
turtle.shape(image)

data_set = pandas.read_csv("50_states.csv")
the_states = data_set["state"].tolist()

is_game_on = True

answers_provided = []

while is_game_on:
    answer_state = screen.textinput(title=f"{len(answers_provided)}/50 states correct", prompt="Tell me one state").title()
    if answer_state in the_states and answer_state not in answers_provided:
        answers_provided.append(answer_state)
        turtle_text = turtle.Turtle()
        turtle_text.hideturtle()
        turtle_text.penup()
        state_data = data_set[data_set["state"] == answer_state]
        turtle_text.goto(int(state_data.x), int(state_data.y))
        turtle_text.write(answer_state)

    if len(answers_provided) == 50:
        is_game_on = False
        print("You did it!!!")

    if answer_state == "Exit":
        is_game_on = False

with open("states to learn.csv", mode="w") as file:
    for state in the_states:
        if state not in answers_provided:
            file.write(f"\n{state}")
