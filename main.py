import pygame
from pygame.draw import *

pygame.init()

FPS = 50
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 1000, 1000))
circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 1)
circle(screen, (255, 0, 0), (240, 170), 15)
circle(screen, (255, 0, 0), (160, 170), 20)
circle(screen, (0, 0, 0), (240, 170), 15, 1)
circle(screen, (0, 0, 0), (160, 170), 20, 1)
circle(screen, (0, 0, 0), (240, 170), 7)
circle(screen, (0, 0, 0), (160, 170), 7)
rect(screen, (0, 0, 0), (160, 220, 80, 15))
polygon(screen, (0, 0, 0), [(90, 100), (100, 90),
                            (190, 150), (180, 160)])
polygon(screen, (0, 0, 0), [(300, 120), (290, 100),
                            (220, 150), (230, 160)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
