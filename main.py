import turtle
import pandas

screen = turtle.Screen()
screen.setup(height=670, width=580)
screen.title("India States Game")
image = "blank_states_image.gif"

screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("31_states.csv")
states_name_list = data.state.to_list()
guessed_states_list = []


while len(guessed_states_list) < 31:
    answer_state = screen.textinput(title=f"{len(guessed_states_list)}/31 States correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        break
    
    if answer_state in states_name_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        answer_state_row = data[data.state == answer_state]
        x_value = int(answer_state_row.x)
        y_value = int(answer_state_row.y)

        t.goto(x=x_value, y=y_value)
        t.write(arg=answer_state, align="left", font=("Arial", 8, "normal"))
        guessed_states_list.append(answer_state)
        states_name_list.remove(answer_state)




# states_to_learn.csv - To create a csv file of the missed out states in the game
states_name_list = data.state.to_list()
not_guessed_states_list = []
for state in states_name_list:
    if state not in guessed_states_list:
        not_guessed_states_list.append(state)


data_list = not_guessed_states_list
data2 = pandas.Series(data_list)

data2.to_csv("states_to_learn.csv")









# # To get x and y co-ordinates in th image.gif
# def on_mouse_click(x, y):
#     print(x,y)

# turtle.onscreenclick(fun=on_mouse_click)
