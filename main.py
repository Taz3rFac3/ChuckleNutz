import pygame
from pygame.locals import *

pygame.init()


screen  = pygame.display.set_mode((1600, 800))

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


