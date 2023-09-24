import math as m


def triangle_square_side(a, b, c):
    p = (a + b + c) / 2
    return m.sqrt(p * (p - a) * (p - b) * (p - c))


def triangle_square_cords(ax, ay, ax1, ay1, bx, by, bx1, by1, cx, cy, cx1, cy1):
    a = m.sqrt(((ax1 - ax) ** 2) + ((ay1 - ay) ** 2))
    b = m.sqrt(((bx1 - bx) ** 2) + ((by1 - by) ** 2))
    c = m.sqrt(((cx1 - cx) ** 2) + ((cy1 - cy) ** 2))
    p = (a + b + c) / 2
    return m.sqrt(p * (p - a) * (p - b) * (p - c))


def round_square(r):
    return m.pi * (r ** 2)
