import pygame

pygame.init()

screen = pygame.display.set_mode()

screen.fill("red")
input("Press enter to continue:")
screen.fill("green")
pygame.display.flip()

# keeps track of display image and next image
