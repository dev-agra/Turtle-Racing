from turtle import Turtle, Screen
from abc import abstractmethod, ABC
import random

screen = Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle would win today?: ")
colors = ['red', 'orange', 'yellow', 'blue', 'purple', 'green']
turtles = []
is_on = False


class TurtleUser(ABC):
    @abstractmethod
    def create_turtle(self):
        pass


class Turtle1(TurtleUser):
    def create_turtle(self):
        tim = Turtle(shape='turtle')
        tim.color(colors[0])
        turtles.append(tim)
        tim.penup()
        tim.goto(x=-280, y=-90)


class Turtle2(TurtleUser):
    def create_turtle(self):
        tim = Turtle(shape='turtle')
        tim.color(colors[1])
        turtles.append(tim)
        tim.penup()
        tim.goto(x=-280, y=-180)


class Turtle3(TurtleUser):
    def create_turtle(self):
        tim = Turtle(shape='turtle')
        tim.color(colors[2])
        turtles.append(tim)
        tim.penup()
        tim.goto(x=-280, y=-270)


class Turtle4(TurtleUser):
    def create_turtle(self):
        tim = Turtle(shape='turtle')
        tim.color(colors[3])
        turtles.append(tim)
        tim.penup()
        tim.goto(x=-280, y=90)


class Turtle5(TurtleUser):
    def create_turtle(self):
        tim = Turtle(shape='turtle')
        tim.color(colors[4])
        turtles.append(tim)
        tim.penup()
        tim.goto(x=-280, y=180)


class Turtle6(TurtleUser):
    def create_turtle(self):
        tim = Turtle(shape='turtle')
        tim.color(colors[5])
        turtles.append(tim)
        tim.penup()
        tim.goto(x=-280, y=270)


t1 = Turtle1()
t1.create_turtle()

t2 = Turtle2()
t2.create_turtle()

t3 = Turtle3()
t3.create_turtle()

t4 = Turtle4()
t4.create_turtle()

t5 = Turtle5()
t5.create_turtle()

t6 = Turtle6()
t6.create_turtle()

if user_bet:
    is_on = True


def racing():
    global is_on
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


racing()
screen.exitonclick()
