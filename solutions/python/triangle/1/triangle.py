def equilateral(sides):
    if all(side <= 0 for side in sides):
        return False

    total = sum(sides)
    is_equilateral = False
    
    for side in sides:
        if total % side == 0:
            is_equilateral = True
        else:
            is_equilateral = False

    return is_equilateral


def isosceles(sides):
    if all(side <= 0 for side in sides):
        return False

    if not is_valid_triangle(sides):
        return False
    
    return (
        sides[0] == sides[1]
        or sides[0] == sides[2]
        or sides[1] == sides[2]
    )


def is_valid_triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    return (
        a > 0
        and b > 0
        and c > 0
        and a + b > c
        and a + c > b
        and b + c > a
    )

def scalene(sides):
    if all(side <= 0 for side in sides):
        return False

    if not is_valid_triangle(sides):
        return False

    return (
        sides[0] != sides[1]
        and sides[0] != sides[2]
        and sides[1] != sides[2]
    )
