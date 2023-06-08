import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Gam")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

letter_state = turtle.Turtle()
letter_state.penup()
letter_state.hideturtle()

"""def get_mouse_click_coord(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coord)"""

# turtle.mainloop()


data = pandas.read_csv("50_states.csv")
list_all_states = data["state"].to_list()

count = 0
all_guessed = False
while not all_guessed:

    answer_state = screen.textinput(title=f"{count}/50, States Correct",
                                    prompt="What's another state's name?").capitalize()
    # Answer_state_lower = answer_state.lower()
    if answer_state == "Exit":
        print("Exit")
        break
    else:
        data = pandas.read_csv("50_states.csv")

        # Checking if the answer is in the map
        checking_answer = data[data["state"] == f"{answer_state}"]
        print(checking_answer)

        checking_answer_if = checking_answer["state"].to_string(index=False)

        if checking_answer_if == answer_state:
            list_all_states.remove(checking_answer_if)

            answer_coo_x = int(checking_answer["x"].to_string(index=False))
            answer_coo_y = int(checking_answer["y"].to_string(index=False))
            print(answer_coo_y)
            print(answer_coo_x)

            # Drawing the answer in the map

            letter_state.goto(answer_coo_x, answer_coo_y)
            letter_state.write(checking_answer["state"].to_string(index=False), align="center",
                               font=("courier", 10, "normal"))

            count += 1

        if count == 50:
            all_guessed = True

dict_states = {'State': list_all_states}

df = pandas.DataFrame(dict_states)
df.to_csv('Missing_states.csv')

print(list_all_states)
