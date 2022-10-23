from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.setpos(-280,280)
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", align="left", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over")