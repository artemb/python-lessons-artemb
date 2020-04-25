from turtle import Screen, Turtle

def new_shape(x, y, color, speed='slowest'):
    t = Turtle()
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.pendown()
    t.speed(speed)
    return t


prev_color = 0


def next_color():
    global prev_color
    colors = ['#f45905', '#c70d3a', '#512c62', '#45969b']
    prev_color += 1
    return colors[prev_color % len(colors)]


def set_up(axis=True, bgcolor='white'):
    s = Screen()
    s.setup(700, 700)
    s.bgcolor(bgcolor)
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
