from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.diff = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.speed("slow")
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.diff *= 0.9

    def reset_pos(self):
        self.diff = 0.1
        self.goto(0,0)
        self.bounce_x()