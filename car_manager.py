from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):  # for cars, we create more object, better to choose separated initialization for each object
        random_choice = random.randint(1, 5)  # random choice helps to reduce number of cars
        if random_choice == 3:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
            new_car.color(self.get_color())  # easier way --> self.color(random.choice(COLORS)),
            # the longer way was just my try
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def get_color(self):
        color = random.choice(COLORS)
        return color

    def move_cars(self):
        for car in self.all_cars:
            new_x = car.xcor()
            new_x -= self.speed
            car.goto(new_x, car.ycor())

    def move_faster(self):
        self.speed += MOVE_INCREMENT  # speed increment does not work so far
