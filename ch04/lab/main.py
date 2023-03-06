import pygame
import random
import math 

pygame.init()


while 1:
  pygame.event.pump()
  width = 600
  height = 600
  hit_box_width = width / 2
  hit_box_height = height / 2

  hitboxes = {
    "red": pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "blue": pygame.Rect(0, 0, hit_box_width, hit_box_height),
  }

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
  pygame.display.flip()
  pygame.time.wait(2000)
  break

number_of_players = 2
radius = 10

colors = ['red', 'green']
w_colors = ['black', 'white']
# colors[0] +=> player1's color
# colors[1] +=> player2's color

player = 0 
results = [0,0]

for i in range(10 * number_of_players):
    x_coord_player = random.randrange(0, 600)
    y_coord_player = random.randrange(0, 600)
    coordinate = (x_coord_player, y_coord_player)
    distance_from_center = math.hypot(center[0] - x_coord_player, center[1] - y_coord_player) #the distance formula
    is_in_circle = distance_from_center <= 600/2 #screen width
   
    if is_in_circle:
        pygame.draw.circle(screen, colors[player], coordinate, radius)
        results[player] += 1
    else:
        pygame.draw.circle(screen, w_colors[player], coordinate, radius)
    pygame.display.flip()
    pygame.time.wait(100)
    player = (player + 1) % 2

    print(results)

font = pygame.font.Font(None, 48)
if results[0] > results[1]:
    text = font.render("Player 1 wins", True, "white")
    screen.blit(text, (0, 0)) # where <x> and<y> are coordinates on screen
elif results[1] > results[0]:
    text = text = font.render("Player 2 wins", True, "white")
    screen.blit(text, (0, 0)) # where <x> and<y> are coordinates on screen
else:
    text = font.render("It is a tie", True, "white")
    screen.blit(text, (0, 0)) # where <x> and<y> are coordinates on screen
pygame.display.flip()
pygame.time.wait(3000)


