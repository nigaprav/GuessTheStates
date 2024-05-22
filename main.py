import turtle, pandas
screen = turtle.Screen()
screen.title("US STATE GAME")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
guessed_states = []
data= pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50" , prompt = "What's another state's name").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    elif answer_state == "Exit":
        break