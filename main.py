import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()



quest = screen.textinput(title="Quest the state", prompt="What another states name?")
correct = set()
while True:

    if quest in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == quest]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(quest)
        correct.add(quest)

    counter = len(correct)
    quest = screen.textinput(title=f"{counter}/50 Quest the state", prompt="What another states name?")

    #turtle.mainloop()










screen.exitonclick()