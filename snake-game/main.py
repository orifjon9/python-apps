import turtle as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

scr = t.Screen()
scr.bgcolor("black")
scr.setup(width=600, height= 600)
scr.title("Snake Game")
scr.tracer(0)

snk = Snake()
board = ScoreBoard()

scr.listen()
scr.onkey(snk.up, "Up")
scr.onkey(snk.down, "Down")
scr.onkey(snk.right, "Right")
scr.onkey(snk.left, "Left")



food = Food()
game_is_on = True
while game_is_on:
    scr.update()
    snk.move()

    if snk.head.xcor() > 280 or snk.head.xcor() < -280 or snk.head.ycor() > 280 or snk.head.ycor() < -280:
        game_is_on = True
        break

    if snk.head.distance(food) < 20:
        food.refresh()
        snk.add_tail()
        scr.update()
        board.scored()
    
    for seg in snk.segments[1:]:
        if snk.head.distance(seg) < 20:
            game_is_on = True
            break

board.game_over()
        
scr.exitonclick()
