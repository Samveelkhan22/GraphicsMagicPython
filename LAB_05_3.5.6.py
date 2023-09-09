import turtle as t

# Set up the turtle
t.speed(1)
t.bgcolor("white")

# Function to draw the motif in part (a)
def draw_motif_a():
    for _ in range(2):
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)

# Function to draw the motif in part (b)
def draw_motif_b():
    t.forward(100)
    for _ in range(3):
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.right(90)

# Function to draw the motif in part (c)
def draw_motif_c():
    for _ in range(4):
        draw_motif_b()
        t.right(90)

# Function to draw the motif in part (d)
def draw_motif_d():
    t.forward(50)
    draw_motif_c()
    t.forward(50)

# Position the turtle and draw the motifs
t.penup()
t.goto(-200, 0)
t.pendown()

# Draw the motifs
draw_motif_a()

t.penup()
t.goto(0, 0)
t.pendown()

draw_motif_b()

t.penup()
t.goto(200, 0)
t.pendown()

draw_motif_c()

t.penup()
t.goto(0, -100)
t.pendown()

draw_motif_d()

# Close the window on click
t.exitonclick()
