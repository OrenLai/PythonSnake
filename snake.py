from turtle import Turtle, Screen

# in python , use all upper case for const variables
TURTLE_X_COORDINATE = [0, -20, -40]
MOVEMENT_STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        # we can only do this after create the snake
        self.head = self.segments[0]

    def create_snake(self):
        """create the snake body"""
        for turtle_x_index in range(0, 3):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(x=TURTLE_X_COORDINATE[turtle_x_index], y=0)
            self.segments.append(tim)

    def move(self):
        """move the snake forward by 20px and get the 2nd and 3rd turtle to move to previous position"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVEMENT_STEPS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
