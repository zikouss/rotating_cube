import pygame
from Cube import *

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


cube = create_cube(200)
n = len(cube)
x, y, z = center_of_gravity(cube)
cube = translation(cube, -x, -y, -z)
rotation_speed = 0.03

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z] or keys[pygame.K_UP]:
        rotate(cube, -rotation_speed, 0, 0)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        rotate(cube, rotation_speed, 0, 0)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        rotate(cube, 0, rotation_speed, 0)
    if keys[pygame.K_q] or keys[pygame.K_LEFT]:
        rotate(cube, 0, -rotation_speed, 0)
    screen.fill((255, 255, 255))
    c = translation(cube, 400, 400, 0)
    draw(screen, c)
    connect_points(screen, c)
    pygame.display.update()
