from turtle import Turtle, Screen
import random as r

competitor_list = []
colors = ["red", "blue", "green", "orange", "grey", "black", "pink", "silver", "gold"]
screen_width = 600
screen_height = 900
TURTLE_SIZE = 2

is_race_on = False
screen = Screen()
screen.setup(width=screen_width, height=screen_height)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt=f"That color is not in the race, enter another color from the list below!\n {' '.join(colors)}: ").lower()

if user_bet:
    is_race_on = True


def create_turtles():
    for i in range(0, len(colors)):
        color_turtle = Turtle("turtle")
        color_turtle.penup()
        color_turtle.turtlesize(TURTLE_SIZE)
        color_turtle.color(colors[i])
        competitor_list.append(color_turtle)


def starting_position(width, height):
    num_compete = len(competitor_list)
    start = width/2 * -1 + 30
    spacing = height / (num_compete + 1)
    start_y = height/2
    for i in range(0, len(competitor_list)):
        start_y -= spacing
        competitor_list[i].goto(x=start, y=start_y)


def racing(turtle):
    random_distance = r.randint(1, 10)
    turtle.forward(random_distance)


create_turtles()
starting_position(width=screen_width, height=screen_height)


while is_race_on:
    for i in range(0, len(competitor_list)):
        racing(competitor_list[i])
        if competitor_list[i].xcor() >= screen_width/2 - (15*TURTLE_SIZE):
            is_race_on = False
            winning_color = competitor_list[i].fillcolor()

if winning_color == user_bet:
    print(f"Congratulations your {user_bet} turtle won!")
else:
    print(f"Sorry the {winning_color} turtle won. You lost!")

screen.exitonclick()
