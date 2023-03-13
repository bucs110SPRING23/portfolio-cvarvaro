import turtle

sides = int(input("Enter number of sides: "))

length = int(input("Enter the length of sides: "))

pen = turtle.Turtle()
pen.color("orange")

window = turtle.Screen()

for s in range(sides):
    pen.forward(length)
    pen.left(360 / sides)

window.exitonclick()
