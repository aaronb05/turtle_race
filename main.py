import random
import turtle
import turtle as t

screen = t.Screen()
screen.setup(width=1000, height=500)
colors = ["red", "blue", "green", "orange", "purple", "yellow"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for tur in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[tur])
    new_turtle.goto(x=-450, y=y_pos[tur])
    all_turtles.append(new_turtle)


def race():

    guess = t.textinput("Turtle", "Which turtle wins the race? enter a color: ")

    racing = True
    while racing:
        for r_turtle in all_turtles:
            r_turtle.forward(random.randint(10, 50))
            if r_turtle.xcor() > 450:
                racing = False
                winner = r_turtle.pencolor()
                if winner == "guess":
                    print(f"You won! The {guess} turtle was the winner!")
                else:
                    print(f"You lost! The {winner} turtle was the winner!")


race()
screen.exitonclick()


