import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    blob = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    blob.shape('turtle')
    # Set your turtle's speed using .speed(2)
    blob.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    blob.color('purple')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)

    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range(4):
        blob.forward(200)
        blob.left(90)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    blob.goto(-100, 100)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    blob.begin_fill()
    blob.circle(50, -360, 50)
    blob.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    blob.goto(100, -100)
    blob.begin_fill()
    blob.forward(100)
    blob.left(64)
    blob.left(97)
    blob.forward(175)
    blob.end_fill()
    blob.penup()
    blob.goto(50, 72)
    blob.pendown()
    blob.begin_fill()
    for i in range(4):
        blob.forward(50)
        blob.right(90)
    blob.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
