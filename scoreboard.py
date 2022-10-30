from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("yellow")
        self.penup()
        with open("score.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.setpos(-280, 280)
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}, highscore: {self.update_highscore()}", align="left",
                   font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over")

    def update_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("score.txt", "w") as data:
                data.write(f"{self.highscore}")

        return self.highscore
