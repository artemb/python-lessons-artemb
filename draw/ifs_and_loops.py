from turtle import Turtle
from draw.drawlib import set_up

s = set_up(axis=True)

t = Turtle()

start_x = 100
start_y = 100

t.penup()
t.goto(start_x, start_y)
t.pendown()

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

s.mainloop()
