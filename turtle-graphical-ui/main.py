import turtle as t
import random


t.colormode(255)
trtl = t.Turtle()
colors = ["red", "green", "blue", "purple", "black", "gray", "orange", "pink", "silver"]

def random_color():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return (r, g, b)


# def draw_shape(number_of_sides:int, color:str):
#     trtl.color(color)
#     for _ in range(number_of_sides):
#         trtl.right(360 / number_of_sides)
#         trtl.forward(100)

# for num_of_sides in range(3, 11):
#     draw_shape(num_of_sides, random.choice(colors))

directions = [0, 90, 180, 270]

trtl.pensize(15)
trtl.speed(0)

for _ in range(200):
    trtl.color(random_color())
    trtl.forward(40)
    trtl.setheading(random.choice(directions))
    

scn = t.Screen()
scn.exitonclick()