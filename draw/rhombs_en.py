# Setting up the drawing screen. You can choose your own colours.
from draw.drawlib import set_up, new_shape, next_color
s = set_up(bgcolor='black', axis=False)
turtle = new_shape(0, 0, 'white', speed='fast')


# To fill a shape with colour, we need to first call begin_fill(),
#   then draw the shape, then call end_fill()
turtle.begin_fill()

# You can call turtle.color() to change the drawing colour.
turtle.color('red')

# Let's draw a diamond shape
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(135)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(135)

# Call end_fill() after the shape is drawn to fill it with colour.
turtle.end_fill()

# The next line helps us prevent the window from closing, so that we can enjoy the result
s.mainloop()

# Task 1.   Using the ` for x in range(N) ` loop remove repeating code lines
#
# Task 2.   Using nested loops draw a shape similar to the example - rhombs.png. You can ignore colour for now.
#
# Task 3.   Using the  next_color() function, fill each diamond shape with it's own colour
#
# Task 4.   Now think of your own shape to draw.
