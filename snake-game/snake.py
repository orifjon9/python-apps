import turtle as t
import time

UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self) -> None:
        self.segments:list[t.Turtle] = []
        self.speed = 0.2
        self.SNAKE_COLOR = "white"
        self.SNAKE_SHAPE = "square"
        self.SNAKE_TAILS_DISTANCE = 20
        self.__create_snake__()
        self.head = self.segments[0]
        
    
    def move(self):
        time.sleep(self.speed)
        for i in range(len(self.segments) - 1, 0, -1):
            new_x, new_y = self.segments[i - 1].xcor(), self.segments[i - 1].ycor()
            self.segments[i].goto(x=new_x, y=new_y)
        self.head.forward(self.SNAKE_TAILS_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.__direct_snake__(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.__direct_snake__(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.__direct_snake__(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.__direct_snake__(LEFT)

    def __direct_snake__(self, heading:int):
        self.head.setheading(heading)
    
    def __create_snake__(self):
        xPos = 0
        for _ in range(3):
            tur = t.Turtle(self.SNAKE_SHAPE)
            tur.penup()
            tur.color(self.SNAKE_COLOR)
            tur.goto(x=xPos, y = 0)
            self.segments.append(tur)
            xPos =-self.SNAKE_TAILS_DISTANCE 