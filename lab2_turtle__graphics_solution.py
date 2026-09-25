"""
Lab 2: Draw some basic shapes with Turtle Graphics, using loop algorithms.

Complete exercise 1-2 (each values 50 points, 100 points in total).

Author:  <your name>
Due Date: This Thursday (Sept. 24) 5:00pm.
    
"""

import turtle
drawing_screen = turtle.Screen()
alex = turtle.Turtle()
"""
Understanding the following three examples is beneficial for you to move to the exercise 1 below.
"""

# Example 1 - Draw 10 steps with each step 20 pixels by 20 pixels.
# num_steps = 10
# alex.speed(5)  # 1 sets the drawing speed as the slowest.
# for _ in range(num_steps): # _ means this loop variable is unused, just repeat loop body num_steps times
#     alex.forward(20) # 20 pixels
#     alex.left(90) # Angle
#     alex.forward(20)
#     alex.right(90)
# alex.shape("blank")  # After drawing, make the alex/pen/brush invisible.


# Example 2 - Draw an equilateral triangle with side length 100 pixels
# Uncomment the line 33 to 41

#alex.clear()  # Clear the previous drawing on the screen.
# alex.speed(1)
# alex.shape("turtle")
# side_length = 100
# exterior_angle = 360 / 3  # Calculate the exterior angle of an equilateral triangle.
# for _ in range(3):
#     alex.forward(side_length)
#     alex.left(exterior_angle)
# alex.shape("blank")


# Example 3 - Draw a square with side length 200 pixels
# Uncomment the line 47 to 57

# alex.clear()  # Clear the previous drawing on the screen.
# alex.shape("arrow")
# alex.up() # alex.up() lifts alex/pen/brush up;
# alex.goto(0, 0) # Go to the center of the drawing screen
# alex.down() # alex.down() puts alex/pen/brush down, ready for drawing.
# side_length = 100
# exterior_angle = 360 / 4  # Calculate the exterior angle of an equilateral triangle.
# for _ in range(4):
#     alex.forward(side_length)
#     alex.left(exterior_angle)
# alex.shape("blank")


'''
Exercise 1 - To draw a regular hexagon:

You may have noticed that to draw a square is very similar 
to draw an equilateral triangle. We need to calculate 
the exterior angle of a square, which is the angle your turtle/pen/brush
will turn.

Now, similar as example 2 and 3, 
but draw a regular hexagon (6 sides) with side length 100.

Hint:
num_sides = 6
exterior_angle = 360 / num_sides
'''

# Code your exe 1 here
alex.clear()  # Clear the previous drawing on the screen.
alex.shape("arrow")
alex.up() # alex.up() lifts alex/pen/brush up;
alex.goto(0, 0) # Go to the center of the drawing screen
alex.down() # alex.down() puts alex/pen/brush down, ready for drawing.
side_length = 100
num_sides = 6
exterior_angle = 360 / num_sides  # Calculate the exterior angle of an equilateral triangle.
for _ in range(num_sides):
    alex.forward(side_length)
    alex.left(exterior_angle)
alex.shape("blank")











"""
Part 2

Understanding the following examples 4, 5 and 6 is beneficial for you to move to the exercise 2 below.
"""

'''
Example 4 
Uncomment the code below in this example, run the file and see the output 
This example clearly demonstrates how to access list elements using loop variable.
'''

# alex.shape('turtle')
# colors = ['red', 'blue', 'orange', 'black']
# for a_color in colors:
#     alex.color(a_color)
#     alex.forward(50) # Loop body is always indented
#     alex.left(90)

'''
Example 5 
Uncomment the code below in this example, run the file and see the output 
This example clearly demonstrates how to access list elements using index.
'''

# alex.shape('turtle')
# colors = ['red', 'blue', 'orange', 'black']
# for i in range(len(colors)):
#     alex.color(colors[i])
#     alex.forward(50) # Loop body is always indented
#     alex.left(90)

'''
Example 6 - Draw a number of concentric circles
Uncomment the code below in this example, run the file and see the output 
This example clearly demonstrates accessing list elements by loop variables.
'''

# num_circles = 7
# rainbow_colors = ["violet", "indigo", "blue",
#                    "green", "yellow", "orange", "red"]
# radius = 30
# radius_increase = 10
# alex.clear()  # Clear the previous drawing on the screen.
# alex.speed(5)
# alex.pensize(5)
# #alex.up()
# for rainbow_color in rainbow_colors:
#     alex.color(rainbow_color)
#     alex.goto(0, -radius)
#     alex.down()
#     alex.circle(radius)
#     radius = radius + radius_increase
#     alex.up()
# alex.shape("blank")



'''
Exercise 2 - To draw a rainbow (like this one https://github.com/awang-capu/comp115_fall2026/blob/main/lab2_rainbow.png):
You can set your own initial radius and increment value.

Hint: You may need to use the functions below:
alex.circle(-radius, 180)
alex.backward()
'''
# Code your exe 2 here

alex.clear()  # Clear the previous drawing on the screen.
radius = 100
increase = 10
alex.pensize(increase)

colors = ['purple', 'darkblue', 'lightblue', 'green', 'yellow', 'orange', 'red']
alex.up()
alex.speed(6)
# for color in colors:
#     alex.color(color)

#     alex.backward(radius) # Forward 100 pixels
#     alex.left(90)
#     alex.down()
#     alex.circle(-radius, 180)
#     alex.left(90)
#     alex.up()
#     alex.backward(radius)

#     radius = radius + increase

alex.left(90)
for color in colors:
    alex.color(color)

    alex.goto(-radius, 0)
    alex.down()
    alex.circle(-radius, 180)
    alex.left(180)
    alex.up()
    radius += increase

alex.shape('blank')









drawing_screen.mainloop() # Wait for the user to close the drawing screen


"""
Please also finish the lab2 quiz on e-learn.
That's all for lab2!
"""
