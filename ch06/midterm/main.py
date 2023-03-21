import turtle

building = turtle.Turtle()
turtle_speed = 2
building.speed(turtle_speed)
window = turtle.Screen()
building.penup()
building.goto(-100,-200)

x_coordinate_start = -70
y_coordinate_start = 110

def draw_building_outline(base, height):
    '''
    This function creates the outline of the building
    Arguments: base is the size of the base, height is how tall the building is 
    '''
    angle = 90
    building.pendown()
    building.fillcolor("maroon")
    building.begin_fill()
    for i in range(2):
        building.forward(base)
        building.left(angle)
        building.forward(height)
        building.left(angle)
    building.end_fill()
    building.penup()
    return base
    return height

def draw_windows(base, height):
    '''
    This function's purpose is to draw the windows of the building
    Arguments: base is the base of the windows, height is the length of the windows height
    '''
    angle = 90
    x_coordinate_start = -70
    y_coordinate_start = 110
    window_start = (x_coordinate_start, y_coordinate_start)
    building.goto(window_start)
    for i in range(2):
        building.pendown()
        building.fillcolor("white")
        building.begin_fill()
        for j in range(2):
            building.forward(base)
            building.left(angle)
            building.forward(height)
            building.left(angle)
        building.penup()
        building.goto(base, y_coordinate_start)
        building.end_fill()
    return base
    return height

def draw_door(base, height):
    '''
    This function's purpose is to draw the door of the building
    Arguments: Base is the door's base and height is the height of the door
    '''
    angle = 90
    building.goto(-15,-200)
    building.pendown()
    building.fillcolor("gray")
    building.begin_fill()
    building.left(angle)
    building.forward(height)
    building.right(angle)
    building.forward(base)
    building.right(angle)
    building.forward(height)
    building.end_fill()
    return base
    return height

def main():
    draw_building_outline(200,400)
    draw_windows(40,60)
    draw_door(30,65)
    window.exitonclick()

main()