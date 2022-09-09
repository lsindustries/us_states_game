import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()




correct = set()
while len(correct) < 50:
    counter = len(correct)
    quest = screen.textinput(title=f"{counter}/50 Quest the state",
                             prompt="What another states name?").title()
    if quest == "Exit":
        missing = []
        for state in all_states:
            if state not in correct:
                missing.append(state)
        new_data = pandas.DataFrame(missing)
        new_data.to_csv("need_to_learn.csv")
        break

    if quest in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == quest]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(quest)
        correct.add(quest)
