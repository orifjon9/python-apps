import turtle as t
import random
colors = ["blue", "red", "black", "green", "purple", "pink", "gray", "orange"]
turtles:list[t.Turtle] = []

scr = t.Screen()
scr.setup(width=500, height=400)

xPos, yPos = -230, -100
for color in colors:
    tur = t.Turtle("turtle")
    tur.color(color)
    tur.penup()
    tur.goto(x=xPos, y=yPos)
    turtles.append(tur)
    yPos +=30

game_over = False
while not game_over:
    for trt in turtles:
        trt.forward(random.randint(5, 20))
        if trt.xcor() >= 230:
            print(f"{trt.pencolor()} won")
            game_over = True
            break
scr.exitonclick()




