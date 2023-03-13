import pygame

pygame.init()

while 1:
    pygame.event.get()
    screen = pygame.display.set_mode()
    dimensions = screen.get_size() 
    starting_point = (dimensions[0] // 2, dimensions[1] // 2)
    
    # draw library
    # where to draw
    # color: "red", [r,g,b]=>[0-255, 0-255, 0-255]
    # starting point: [x, y] 
    # radius: 50

    radius = 200
    for _ in range(3):
        pygame.draw.circle(screen, "blue", starting_point, radius)
        starting_point[1] = starting_point[1] - radius
        radius = radius // 2
        starting_point[1] = starting_point[1] - radius
    
    pygame.display.flip()
    pygame.time.wait(5000)
    
    break



