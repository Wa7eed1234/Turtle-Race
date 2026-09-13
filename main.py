import time
from turtle import Screen
from player import Player
from cars import Cars
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross The Road Game")
screen.tracer(0)

# Create player
player = Player()

# Control player
screen.listen()
screen.onkeypress(player.move, "Up")

# create cars
cars = Cars()

# Create Scoreboard
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    # Create and move car
    cars.make_car()
    cars.move()

    # if the turtle hit the car
    for car in cars.all_cars:
        if player.distance(car) < 21:
            score.game_over()
            game_is_on = False

    # update the scoreboard on finish line
    if player.is_at_finish_line():
        player.go_to_start()
        cars.increase_speed()
        score.update_scoreboard()
        score.increase_score()


screen.exitonclick()

