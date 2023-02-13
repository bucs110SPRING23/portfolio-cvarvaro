import pygame

while 1:
    screen = pygame.display.set_mode(200, 200)
    pygame.draw.circle(screen, "blue", [200, 150], 50)
    pygame.display.flip()

    pygame.time.wait(5000)



