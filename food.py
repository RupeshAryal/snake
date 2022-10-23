from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.penup()

    def location(self):
        random_x = random.randint(-270,270)
        random_y = random.randint(-270,270)
        self.goto(random_x, random_y)



