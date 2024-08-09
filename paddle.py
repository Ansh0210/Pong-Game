from turtle import Turtle

# P_RIGHT_X_COR = 350
# P_LEFT_X_COR = -350
MOVE_DISTANCE = 50


class Paddle(Turtle):

    def __init__(self, cor_x_y):
        super().__init__()
        self.cor_x = cor_x_y[0]
        self.cor_y = cor_x_y[1]
        self.create_paddle()
        # self.shape("square")
        # self.color("white")
        # self.penup()
        # self.setheading(90)
        # self.shapesize(stretch_wid=1, stretch_len=5)
        # self.speed("fastest")
        # self.goto(x=P_RIGHT_X_COR, y=0)
        self.goto(x=self.cor_x, y=self.cor_y)

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        # self.speed("fastest")

    def move_up(self):
        # self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        # self.setheading(270)
        self.backward(MOVE_DISTANCE)

    def reset_paddle_pos(self):
        self.goto(x=self.cor_x, y=self.cor_y)

