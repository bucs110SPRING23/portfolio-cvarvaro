import pygame

# Part A
def threenp1(n):
    count = 0
    while n > 1.0:
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
       count += 1
    return count

def threenp1range(upper_limit):
    objects_in_sequence = {}
    for i in range(2, upper_limit + 1):
       variable = threenp1(i)
       objects_in_sequence[i] = variable
    return objects_in_sequence

#Part B
def graph_coordinates(threenplus1_iters_dict):
    coordinates = list(threenplus1_iters_dict.items())
    print(coordinates)
    window = pygame.display.set_mode(size=(640, 480))
    window.fill("white")
    pygame.draw.lines(window, "black", True, points=coordinates)
    new_display = pygame.transform.flip(window, False, True)
    window.blit(new_display, (0, 0))

    width, height = new_display.get_size()
    factor = 2
    print((width * factor, height * factor))
    new_display = pygame.transform.scale(new_display, (width * factor, height * factor))
    window.blit(new_display, (width * factor, height * factor))
    # max_so_far = 0
    pygame.display.flip()
    # pygame.time.wait(5000)


def main():
   dictionary = threenp1range(100)
   print(dictionary)
   graph_coordinates(dictionary)


pygame.init()

while 1:
    pygame.event.pump()
    main()
    pygame.time.wait(5000) #2 seconds pause before ending the program. Increase if needed.
    break