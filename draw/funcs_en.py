# Setting up the drawing canvas.
from draw.drawlib import set_up, new_shape
s = set_up(bgcolor='black', axis=False)

# We will draw a rectangle
# The variables below set up the rectangle's parameters - position, color and size
start_x = 0
start_y = 0
color = 'yellow'
size_x = 50
size_y = 100

# Now let's begin drawing
turtle = new_shape(start_x, start_y, color, speed='fast')
turtle.begin_fill()

for x in range(2):
    turtle.forward(size_x)
    turtle.left(90)
    turtle.forward(size_y)
    turtle.left(90)

turtle.end_fill()
# We are hiding the turtle so that we just see the shape
turtle.hideturtle()

# The next command prevents the window from closing, so that we can enjoy our result
s.mainloop()

# Задача 1. Great, we have an algorithm that draws a rectangle.
#           Change the parameters and draw the rectangle in another location with another size and colour.
#
# Задача 2. And now try to draw 2 rectangles on the same screen in different places and of different size and colour.
#
# Задача 3. Write a function that draws a rectangle with a given location, size and colour.
#           Here is how you can define a function: def function_name (param1, param2):
#           Using your new function, draw 4 different rectangles in 4 different locations
#
# Задача 4. Now write a function to draw a triangle. And another one to draw a circle.
