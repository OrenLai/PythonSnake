from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(0, 280)

    def show_score(self):
        self.clear()
        self.write(f"score:{self.score}", False, align="center")
