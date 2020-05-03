# Now it's time to put all your knowledge together
# We will write a program that pains a picture.
#
# Task 1.       First - let us create all the functions that we may need: rectangle, circle, triangle.
#               Write and test your functions.
#               Each function needs to accept a starting position, size and colour
#
# Task 2.       Using your functions, paint a picture
#               Here is an example, but please feel free to draw your own:
#               Green grass, blue sky, yellow sun, a tree and a house.
#
# Hints.        Here is how your define a function: def function_name(param1, param2):
#               Here is how you create a loop: for x in range(N):
#               Here is how you start drawing a new shape: turtle = new_shape(x, y, color, 'fastest')
#               You can use colour names or colour codes, like this: #5BC0BE
#               You can find some nice colours with their codes here: https://coolors.co/generate
#               To fill a shape you need to call ` turtle.begin_fill() ` before drawing a shape, and turtle.end_fill() - after
#               To hide the turtle call turtle.hideturtle()
#               The size of the canvas is - 700 х 700. The 0, 0 point is in the middle. (-350, -350) is the bottom left corner.

from draw.drawlib import set_up, new_shape
s = set_up(bgcolor='black', axis=False)




s.mainloop()
