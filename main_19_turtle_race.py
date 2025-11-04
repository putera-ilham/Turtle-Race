import turtle
from turtle import Turtle, Screen
import random


screen = Screen()

# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     tim.setheading(tim.heading() + 10)
#
# def turn_right():
#     tim.setheading(tim.heading() - 10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(move_forwards, "w" )
# screen.onkey(move_backwards, "s" )
# screen.onkey(turn_left, "a" )
# screen.onkey(turn_right, "d" )
# screen.onkey(clear, "c" )



### ---------------------------------------- TURTLE RACE -------------------------------------------- ###

### --- Screen SETUP --- ###

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                 prompt="Which turtle will claim the race? Enter a color: ")


### --- TURTLES SETUP --- ###

all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]

for turtle_i in range(0, 6):
    new_t = Turtle(shape="turtle")
    new_t.penup()
    new_t.color(colors[turtle_i])
    new_t.goto(x=-230, y=y_pos[turtle_i])
    all_turtles.append(new_t)


### --- MAIN RACE --- ###

if user_bet:
    is_racing = True

while is_racing:
    for t in all_turtles:
        if t.xcor() > 230:
            is_racing = False
            winning_c = t.pencolor()
            if winning_c == user_bet:
                print(f"You've won. The {winning_c} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_c} turtle is the winner!")

        rand_dist = random.randint(0, 10)
        t.forward(rand_dist)


### --- Exit screen on click --- ###

screen.exitonclick()

