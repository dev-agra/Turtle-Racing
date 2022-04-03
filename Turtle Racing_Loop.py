from turtle import Turtle, Screen
import random

is_on = False
screen = Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle would win today?: ")
colors = ['red', 'orange', 'yellow', 'blue', 'purple', 'green', 'brown']
y_postions = [180, 120, 60, 0, -60, -120, -180]
turtles = []

for turtle_index in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=y_postions[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_on = True

while is_on:
    for turtle in turtles:
        if turtle.xcor() > 280:
            winning_color = turtle.pencolor()
            is_on = False
            if winning_color == user_bet:
                print(f"You WON! {winning_color} is the winner")
            else:
                print(f"You LOST! {winning_color} is the winner")
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

screen = Screen()
screen.exitonclick()
