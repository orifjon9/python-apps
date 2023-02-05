from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__() # type: ignore
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))