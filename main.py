from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

rupesh = Snake()

food = Food()
screen.update()
food.location()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=rupesh.move_up)
screen.onkey(key="Down", fun=rupesh.move_down)
screen.onkey(key="Right", fun=rupesh.move_right)
screen.onkey(key="Left", fun=rupesh.move_left)

game_on = True
while game_on:
    Screen().update()
    time.sleep(0.09)
    rupesh.move()
    if rupesh.head.distance(food) < 15:
        food.location()
        scoreboard.update()
        rupesh.update_snake()
    if abs(rupesh.head.xcor()) > 290 or abs(rupesh.head.ycor()) > 290:
        game_on = False
        scoreboard.game_over()
    for segment in rupesh.segments:
        if segment == rupesh.head:
            pass
        elif segment.distance(rupesh.head) < 10:
            game_on = False
            scoreboard.game_over()



screen.exitonclick()
