import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)

rgb_colors = []
color_list = colorgram.extract('image.jpg', 30)

for color in color_list:
    rgb_colors.append((color.rgb.r, color.rgb.b, color.rgb.g))


timmy = turtle_module.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

# Move start from center of screen to lower left
timmy.setheading(225)
timmy.forward(325)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()