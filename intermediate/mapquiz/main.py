import turtle
import pandas

data = pandas.read_csv("/Users/anirudhmulky/Desktop/python/mapquiz/states.csv")
all_states = data.state.to_list()
guessed = []
screen = turtle.Screen()
screen.title("India map game")
image = "/Users/anirudhmulky/Desktop/python/mapquiz/india.gif"
screen.addshape(image)
turtle.shape(image)
while len(guessed) < 30:
    answer = screen.textinput(title=f"{len(guessed)}/29 states correct", prompt="Name any state").title()


    if answer in all_states:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        statedata = data[data.state == answer]
        t.goto(statedata.x.item(),statedata.y.item())
        t.write(answer)

screen.exitonclick()

