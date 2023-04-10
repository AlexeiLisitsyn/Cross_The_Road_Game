from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1

    def update_level(self):
        self.goto(y=250, x=-200)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
