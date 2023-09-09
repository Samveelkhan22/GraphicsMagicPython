import turtle as t

# Set up the turtle
t.speed(1)
t.bgcolor("white")

# Function to draw the meander in part (a)
def draw_meander_a():
    for _ in range(2):
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)

# Function to draw the meander in part (b)
def draw_meander_b():
    t.forward(100)
    for _ in range(3):
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.right(90)

# Position the turtle and draw the meanders
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw the meanders
draw_meander_a()

t.penup()
t.goto(150, 0)
t.pendown()

draw_meander_b()

# Close the window on click
t.exitonclick()
