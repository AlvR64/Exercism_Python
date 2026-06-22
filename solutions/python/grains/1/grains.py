def square(number):
    
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    if number == 1:
        return 1
    
    return 2 ** (number - 1)


def total():
    total_grains = 0
    for a in range(1, 65):
        total_grains += square(a)

    return total_grains
