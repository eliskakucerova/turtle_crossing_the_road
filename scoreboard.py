from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.hideturtle()
        self.penup()
        self.color('black')
        self.setposition(0, 260)

        self.score = 0
        self.write(f"Score: {self.score}", align='center', font=FONT)

    def win(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align='center', font=FONT)

    def game_over(self):
        self.clear()
        self.setposition(0, 0)
        self.write("GAME OVER", align='center', font=FONT)


# TODO write the board for the highest point so far reached
