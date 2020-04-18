from turtle import Screen, Turtle


def set_up(axis=True):
    s = Screen()
    s.setup(700, 700)
    if axis:
        axis_drawer = Turtle()
        axis_drawer.color('#A4AEF3')
        axis_drawer.speed('fastest')
        axis_drawer.penup()
        axis_drawer.goto(- s.window_width() / 2 + 30, 0)
        axis_drawer.pendown()
        axis_drawer.goto(s.window_width() / 2 - 30, 0)
        axis_drawer.stamp()
        axis_drawer.penup()
        axis_drawer.goto(0, - s.window_height() / 2 + 30)
        axis_drawer.setheading(90)
        axis_drawer.pendown()
        axis_drawer.goto(0, s.window_height() / 2 - 30)
        axis_drawer.stamp()
        axis_drawer.penup()
        axis_drawer.hideturtle()
        axis_drawer.goto(-s.window_width() / 2 + 30, 5)
        axis_drawer.write(f"-{int(s.window_width() / 2)}")
        axis_drawer.goto(s.window_width() / 2 - 50, 5)
        axis_drawer.write(f"+{int(s.window_width() / 2)}", )
        axis_drawer.goto(5, -s.window_height() / 2 + 30)
        axis_drawer.write(f"-{int(s.window_height() / 2)}")
        axis_drawer.goto(5, s.window_height() / 2 - 30)
        axis_drawer.write(f"+{int(s.window_height() / 2)}")

    return s
