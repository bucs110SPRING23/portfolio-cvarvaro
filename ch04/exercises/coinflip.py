import turtle
import random

turt = turtle.Turtle()
turt.shape("turtle")
turt.speed(0)
wn = turtle.Screen()

angle = 90
coin_flip = random.randrange(0,2)
distance = 10
colors = ["yellow", "red", "blue"]
while True:
    coin_flip()
    if coin_flip:
        turt.right(angle)
    else:
        turt.left(angle)
    turt.forward(distance)
    
    turtleX = turt.xcor()
    turtleY = turt.ycor()

    x_range = wn.window_width() / 2
    y_range = wn.window_height() / 2

    turt.color(random.choice(colors))