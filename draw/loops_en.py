from draw.drawlib import set_up, new_shape
screen = set_up(axis=True)

turtle = new_shape(100, 100, 'blue')

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

screen.mainloop()


# Task 1.   The turtle draws a square, but the code repeats itself
#           Using the for in range(N) loop, remove code repetition
#
# Task 2.   Try and draw a triangle. A hexagon. An octagon
#
# Task 3.   Drawing regular polygons looks very similar.
#           The only thing that is changing is the number of edges.
#           Create a variable to store the number of edges.
#           Change the code to draw any number of edges.
