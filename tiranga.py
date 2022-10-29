#import colorgram

#rgb_colors = []

#colors = colorgram.extract('indian flag.jpeg', 4)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#
#print(rgb_colors)
color_list = [(252, 118, 0), (20, 135, 9), (254, 254, 253), (52, 68, 147)]
#import turtle
import turtle
from turtle import *

# screen for output
screen = turtle.Screen()
# Defining a turtle Instance
t = turtle.Turtle()
speed("fastest")

# initially penup()
t.penup()
t.goto(-200, 125)
t.pendown()
# Orange Rectangle
#white rectangle
t.color("orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(84)
t.right(90)
t.forward(400)
t.end_fill()
t.left(90)
t.forward(84)

# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(84)
t.left(90)
t.forward(400)
t.left(90)
t.forward(84)
t.end_fill()

# Big Blue Circle
t.penup()
t.goto(35, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(35)
t.end_fill()

# Big White Circle
t.penup()
t.goto(30, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()

#Mini Blue Circles of Flag
t.penup()
t.goto(-27, -4)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(2)
    t.end_fill()
    t.penup()
    t.forward(7)
    t.right(15)
    t.pendown()

# Small Blue Circle
t.color("navy")
t.penup()
t.goto(10, 0)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

#The spokes of India Flag
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(1)
for i in range(24):
    t.forward(30)
    t.backward(30)
    t.left(15)

#for stick of the flag
t.color("Brown")
t.pensize(10)
t.penup()
t.goto(-200,125)
t.right(180)
t.pendown()
t.forward(800)

#for rope on the stick
t.penup()
t.goto(-200,125)
t.pendown()
turtle.colormode(255)
t.color(204, 204, 0)
t.right(90)
for _ in range(50):
    t.circle(13, 180)
    t.circle(-13, 180)

#to hold the
#output window
turtle.done()

