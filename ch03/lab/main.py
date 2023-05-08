import random
import pygame
import math

# Part A
pygame.init()

while 1:
  pygame.event.pump()
  
  screen = pygame.display.set_mode((600,600))
  screen_size_variable = pygame.display.get_window_size()
  center = (screen_size_variable[0] // 2, screen_size_variable[1] // 2)
  
  vertical_line_start = (300,600)
  vertical_line_end = (300,0)
  horizontal_line_start = (0,300)
  horizontal_line_end = (600,300)

  screen.fill("yellow")
  pygame.draw.circle(screen, "light blue", center, screen_size_variable[1] // 2)
  pygame.draw.circle(screen, "black", center, screen_size_variable[1] // 2, 5)
  pygame.draw.line(screen, "black", vertical_line_start, vertical_line_end)
  pygame.draw.line(screen, "black", horizontal_line_start, horizontal_line_end)
  break

# Part B

radius = 10
for i in range(10):
    x_coord = random.randrange(0, 600)
    y_coord = random.randrange(0, 600)
    coordinate = (x_coord, y_coord)
    distance_from_center = math.hypot(center[0] - x_coord, center[1] - y_coord) #the distance formula
    is_in_circle = distance_from_center <= 600/2 #screen width
   
    if is_in_circle:
        pygame.draw.circle(screen, "red", coordinate, radius)
        pygame.display.flip()
        pygame.time.wait(1000)
    else:
        pygame.draw.circle(screen, "black", coordinate, radius)
        pygame.display.flip()
        pygame.time.wait(1000)

    #2 seconds pause before ending the program. Increase if needed.