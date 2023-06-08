from turtle import Turtle

STARTTNG_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
    
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTTNG_POSITION)


    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False