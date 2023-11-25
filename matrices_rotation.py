from math import sin, cos


def rotation_x(angle):
    mat = [[1, 0, 0], [0, cos(angle), -sin(angle)], [0, sin(angle), cos(angle)]]
    return mat


def rotation_y(angle):
    mat = [[cos(angle), 0, sin(angle)], [0, 1, 0], [-sin(angle), 0, cos(angle)]]
    return mat


def rotation_z(angle):
    mat = [[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]]
    return mat
