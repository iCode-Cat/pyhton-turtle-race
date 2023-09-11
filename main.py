from turtle import Turtle, Screen
import random

is_race_on = False
color_exists = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter a color:")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50 , 80]
all_turtles = []

while color_exists == False:
    for cl in colors:
        if cl == user_bet:
            color_exists = True
    if color_exists == False:
        user_bet = screen.textinput(title="Make your bet", prompt="Enter a color:")

for turtle_index in range(0, len(colors)):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for player in all_turtles:
        random_distance = random.randint(0, 10)
        player.forward(random_distance)
        player_pos = player.position()
        if player_pos[0] > 219:
            winner_color = player.color()[0]
            is_race_on = False
            print(f"{winner_color} is the winner!")
            if winner_color == user_bet:
                print('You won!')
            else:
                print('You lost!')


screen.exitonclick()