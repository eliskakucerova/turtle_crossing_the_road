from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()  # for player, we inherit
        self.shape('turtle')
        self.color('pink')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.ycor()
        new_y += MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def beginning(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def refresh(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True  # the condition in beginning(self) can not be written here, return True does not work
        else:
            return False

# TODO def go_down() for player by button 'DOWN'
