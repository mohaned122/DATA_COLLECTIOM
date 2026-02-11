import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Turtle Spiral")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # fastest
turtle.colormode(255)  # allow RGB colors

# Function to generate rainbow colors
def rainbow_colors(n):
    colors = []
    for i in range(n):
        color = colorsys.hsv_to_rgb(i/n, 1, 1)  # HSV to RGB
        colors.append((int(color[0]*255), int(color[1]*255), int(color[2]*255)))
    return colors

colors = rainbow_colors(100)

# Draw a spiral
for i in range(200):
    t.color(colors[i % 100])
    t.forward(i * 2)
    t.right(59)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
