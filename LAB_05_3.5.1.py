import turtle as t

# Set up the turtle
t.speed(1)
t.bgcolor("white")

# Function to draw the figure in part (a)
def draw_figure_a():
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)

# Function to draw the figure in part (b)
def draw_figure_b():
    for _ in range(4):
        draw_figure_a()
        t.right(90)

# Function to draw the figure in part (c)
def draw_figure_c():
    for _ in range(6):
        draw_figure_b()
        t.right(60)

# Position the turtle and draw the figures
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw the figures
draw_figure_a()

t.penup()
t.goto(150, 0)
t.pendown()

draw_figure_b()

t.penup()
t.goto(0, -200)
t.pendown()

draw_figure_c()

# Close the window on click
t.exitonclick()
