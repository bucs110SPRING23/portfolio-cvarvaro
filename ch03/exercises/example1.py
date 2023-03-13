# bool - boolean value
# True or False

# print(type(True))
# print(bool(1), bool(-1), bool("hello"))
# print(bool(0), bool(""), bool([]))

# # boolean expressions
# x = 5
# y = 10

# print(x == y) # equality, == bolean equality test, = is assignment
# print(x > y)
# print(x < y) 
# print(x >= y)
# print(x <= y)

# # and, or, not - semantic operators
# # and: and == True, when x and y are both True

# print(True and True)
# print(True and False) 
# print(False and True)
# print(False and False)

# print(True or True)
# print(True or False) 
# print(False or True)
# print(False or False)

# not - negation

# num = int(input("Num: "))
# for i in range(3):
#     if num % 3 == 0:
#         print("fizz")
#     elif num % 5 == 0:
#         print("buzz")
#     elif num % 5 == 0 and num % 3 == 0:
#         print("fizzbuzz")
# for i in range(num + 1):
#     if i % 3 == 0
import random
import pygame
pygame.init()
screen = pygame.display.set_mode()
colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)
for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(1000)
    
    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(250)

message = """
    Simon says:
    UP: RED
    DOWN: BLUE
    LEFT: GREEN
    RIGHT: YELLOW
    
    click on the window, enter a sequence, m then press enter
    """

response = input(message)

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            print("UP")
        elif event.key == pygame.K_DOWN:
            print("DOWN")
        elif event.key == pygame.K_LEFT:
            print("LEFT") 