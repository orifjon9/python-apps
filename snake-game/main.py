import turtle as t
from snake import Snake

scr = t.Screen()
scr.bgcolor("black")
scr.setup(width=600, height= 600)
scr.title("Snake Game")
scr.tracer(0)

snk = Snake()

scr.listen()
scr.onkey(snk.up, "Up")
scr.onkey(snk.down, "Down")
scr.onkey(snk.right, "Right")
scr.onkey(snk.left, "Left")

game_is_on = True
while game_is_on:
    scr.update()
    snk.move()

        
scr.exitonclick()