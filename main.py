import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# objects calling
player = Player()
car = CarManager()
board = Scoreboard()

# moving with the player up
screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    car.create_car()
    car.move_cars()

    # crush player vs. car
    for vehicle in car.all_cars:
        if vehicle.distance(player) < 25:  # note for me, incorrectly written condition vehicle vs. player
            game_is_on = False
            board.game_over()
            break

    player.refresh()

    if player.refresh():
        player.beginning()
        board.win()
        car.move_faster()

    time.sleep(0.5)
    screen.update()
