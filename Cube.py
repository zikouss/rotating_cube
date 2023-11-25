import pygame
from matrix_rotation import *
from matrix_operations import *


def create_cube(size):
    cube = [
        [[0], [0], [0]],
        [[size], [0], [0]],
        [[0], [size], [0]],
        [[0], [0], [size]],
        [[size], [0], [size]],
        [[0], [size], [size]],
        [[size], [size], [0]],
        [[size], [size], [size]],
    ]
    return cube


def center_of_gravity(cube):
    avg_x = sum(point[0][0] for point in cube) / len(cube)
    avg_y = sum(point[1][0] for point in cube) / len(cube)
    avg_z = sum(point[2][0] for point in cube) / len(cube)
    return avg_x, avg_y, avg_z


def translation(cube, x, y, z):
    n = len(cube)
    c = cube.copy()
    for i in range(n):
        c[i] = [[cube[i][0][0] + x], [cube[i][1][0] + y], [cube[i][2][0] + z]]
    return c


def draw(screen, cube):
    for point in cube:
        pygame.draw.circle(screen, (0, 0, 0), (point[0][0], point[1][0]), 5)


def connect_points(screen, cube):
    connections = [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 4),
        (1, 6),
        (2, 6),
        (3, 5),
        (3, 4),
        (4, 7),
        (5, 7),
        (6, 7),
        (2, 5),
    ]
    for i, j in connections:
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (cube[i][0][0], cube[i][1][0]),
            (cube[j][0][0], cube[j][1][0]),
            2,
        )


def rotate(cube, x, y, z):
    n = len(cube)
    r_x = rotation_x(x)
    r_y = rotation_y(y)
    r_z = rotation_z(z)
    for i in range(n):
        cube[i] = matrix_product(r_x, cube[i])
        cube[i] = matrix_product(r_y, cube[i])
        cube[i] = matrix_product(r_z, cube[i])
