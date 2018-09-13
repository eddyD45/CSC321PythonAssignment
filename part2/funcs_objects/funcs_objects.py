from math import sqrt


def distance(point1, point2):
    xDistance = point2.x - point1.x
    yDistance = point2.y - point1.y
    return sqrt((xDistance ** 2) + (yDistance ** 2))

def circles_overlap(circle1, circle2):
    return (circle1.radius + circle2.radius) > distance(circle1.center, circle2.center)
