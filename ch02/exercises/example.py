import pygame

pygame.init()

screen = pygame.display.set_mode()

screen.fill("red")
pygame.time.wait(1000)
pygame.display.flip()
screen.fill("green")
pygame.display.flip()
pygame.time.wait(1000)
screen.fill("blue")
pygame.display.flip()
pygame.time.wait(1000)

screen_size = screen.get_size()

# [z, y, width, height]
dimensions = [screen_size[0] / 2, screen_size[1] / 2, 250, 250]
pygame.draw.rect(screen, "red", dimensions)

# [x, y, width, height]
dimensions = [300, 300, 250, 250]
pygame.draw.rect(screen, "blue", dimensions)

pygame.display.flip()


