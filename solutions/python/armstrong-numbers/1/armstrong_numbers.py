def is_armstrong_number(number):
    digits = list(str(number))

    num = 0
    power = len(digits)
    
    for digit in digits:
        num += int(digit) ** power

    if num != number:
        return False
    else :
        return True
    