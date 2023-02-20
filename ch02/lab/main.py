import random
import turtle
import pygame
import math

#Part A
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

turtle1.penup()
turtle2.penup()

turtle1.goto(100,20)
turtle2.goto(100,-20)

turtle1.goto(random.randrange(1,101),20)
turtle2.goto(random.randrange(1,101),20)

pygame.time.wait(100)

turtle1.goto(100,20)
turtle2.goto(100,-20)
turtle1.pendown()
turtle2.pendown()

for i in range(10):
    turtle1.goto(turtle.xcor()+ random.randrange(1, 11),20)
    turtle2.goto(turtle.xcor()+ random.randrange(1, 11),20)


#Part B
pygame.init()
window = pygame.display.set_mode()

def shape(window, number_sides):
    coordinates = []
    number_sides = number_sides
    side_length = 100
    offset = 100
    for i in range(number_sides):
        angle = (2.0 * math.pi)/number_sides
        x_side = side_length * math.cos(angle * i) + offset
        y_side = side_length * math.sin(angle * i) + offset
        coordinates.append([x_side, y_side])
    window.fill('black')
    pygame.draw.polygon(window, "white", coordinates)
    pygame.display.flip()
    pygame.time.delay(1000)

for num_sides in [3,4,6,20,100,360]:
    shape(window, num_sides)

