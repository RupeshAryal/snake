from turtle import Turtle, Screen


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        self.segments = []
        first_snake = Turtle("square")
        first_snake.color("white")
        first_snake.penup()

        self.segments.append(first_snake)
        tail = first_snake

        for i in range(0, 2):
            next_snake = Turtle("square")
            next_snake.color("white")
            next_snake.penup()
            next_snake.setpos(tail.xcor() - 20, tail.ycor())
            self.segments.append(next_snake)

    def update_snake(self):
        add_snake = Turtle("square")
        add_snake.color("white")
        add_snake.penup()
        add_snake.setpos(self.tail.xcor() - 20, self.tail.ycor())
        self.segments.append(add_snake)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[segment - 1].xcor()
            y_cor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_cor, y_cor)

        self.segments[0].forward(20)

    def move_up(self):
        if self.segments[0].heading() == 0:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].right(90)

    def move_left(self):
        if self.segments[0].heading() == 270:
            self.segments[0].right(90)
        else:
            self.segments[0].left(90)

    def move_right(self):
        if self.segments[0].heading() == 270:
            self.segments[0].left(90)
        else:
            self.segments[0].right(90)

    def move_down(self):
        if self.segments[0].heading() == 0:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].left(90)
