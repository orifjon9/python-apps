from turtle import Turtle

FONT_COLOR = "white"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.goto(x=0, y=270)
        self.score = 0
        self.color(FONT_COLOR)
        self.penup()
        self.hideturtle()
        self.refresh()
    
    def scored(self):
        self.score += 1
        self.refresh()
    
    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}",align="center", font=FONT)
    
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER",align="center", font=FONT)
    