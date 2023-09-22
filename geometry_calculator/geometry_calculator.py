import math

def circle_area(radius):
    return math.pi * radius**2

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def get_shape_area(*args):
    if len(args) == 1:
        return circle_area(args[0])
    elif len(args) == 3:
        return triangle_area(*args)
    else:
        raise ValueError("Неподдерживаемое количество аргументов")
