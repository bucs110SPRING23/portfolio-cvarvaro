import pygame

# Part A
def threenp1(n):
    while n > 1.0:
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return None

def threenp1range(upper_limit):
    objects_in_sequence = {}
    for i in range(2, upper_limit):
       variable = threenp1(i)
       objects_in_sequence[i] = variable
    return objects_in_sequence

#Part B
def graph_coordinates(threenplus1_iters_dict):
   pygame.init()
   window = pygame.display.set_mode()
   window.fill("white")
   new_display = pygame.transform.flip(window, False, True)
   width, height = new_display.get_size()
   factor = 2
   new_display = pygame.transform.scale(new_display, (width * factor, height * factor))
   window.blit(new_display, (0, 0))
   max_so_far = 0
#    for i in range(threenplus1_iters_dict):
