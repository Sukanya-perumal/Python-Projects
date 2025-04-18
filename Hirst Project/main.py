import random
from turtle import Turtle,Screen
import turtle as tim
tim.colormode(255)
color_list = [(29, 41, 60), (49, 92, 143), (145, 81, 44),(170, 14, 28), (160, 56, 87), (227, 154, 8), (209, 162, 105),
              (235, 217, 75), (66, 30, 43), (236, 240, 246),(37, 142, 47), (222, 225, 4), (48, 36, 30), (46, 47, 96),
              (95, 193, 168), (120, 161, 172), (19, 54, 47),(243, 89, 22), (161, 16, 13), (18, 97, 45), (212, 58, 79),
              (49, 169, 80), (189, 146, 159), (231, 173, 186), (226, 177, 168), (45, 153, 195), (160, 212, 184)]

t = Turtle()
t.speed("fastest")
t.hideturtle()
t.penup()
t.goto(-200,-200)
# t.pendown()
def draw_dot_row(t, num_dots, dot_size, spacing ):
    for _ in range(num_dots):
        t.dot(dot_size,random.choice(color_list))
        # t.penup()
        t.forward(spacing)
        # t.pendown()
draw_dot_row(t,10,20,50)
for i in range(1,10):
    if i %2 ==0:
        t.penup()
        for _ in range(2):
            t.right(90)
            t.forward(50)
        # t.pendown()
        draw_dot_row(t,10,20,50)
    else:
        t.penup()
        for _ in range(2):
            t.left(90)
            t.forward(50)
        draw_dot_row(t, 10, 20, 50)



screen = Screen()
screen.exitonclick()