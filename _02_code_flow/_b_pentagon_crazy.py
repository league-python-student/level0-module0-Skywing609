import random
import turtle


# Returns a random color!
from turtle import Turtle


def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


def get_next_color(i):
    return colors[i % len(colors)]


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('black')
    window.setup(width=0.75, height=0.9, startx=0, starty=0)
    
    colors = ('hotpink', 'pink', 'purple', 'blue', 'white', 'light blue')
    
    # Make a new turtle
    blob = turtle.Turtle()  # type: Turtle
    # Make the turtle shape 'turtle', .shape('turtle')
    blob.shape('turtle')
    # Set the turtle speed to max (0)
    blob.speed(0)
    # Set the turtle width to 1
    blob.width(1)
    # Create a variable to hold the number of sides in a pentagon
    penta = 4
    # Create a variable to be the angle of 360 divided by the sides variable
    angle = 360/4
    # Use a for loop to repeat ALL the following lines of code 360 times. 
    for i in range(900):
        if i==100:
            blob.width(2)
        if i==200:
            blob.width(3)
        blob.color(get_next_color(i))
        blob.forward(i)
        blob.right(angle+1)
    blob.hideturtle()
        # If the loop variable (i) is equal to 100, set the turtle width to 2
        
        # If the loop variable (i) is equal to 200, set the turtle width to 3
        
        # Use the get_next_color function to set the turtle pencolor,
        # *hint .pencolor(get_next_color(i))
        
        # Move the turtle forward by the loop variable, *hint .forward(i)
        
        # Turn the turtle to the right by the angle variable + 1

    # Hide your turtle so you can see the pattern.
        
    # Check the pattern against the picture in the recipe. If it matches, you are done!
    
    # Variations:
    # *Make the pattern really huge
    # *Change the colors
    # *Experiment with different shapes
    
    # Call the turtle.done() method
    turtle.done()
