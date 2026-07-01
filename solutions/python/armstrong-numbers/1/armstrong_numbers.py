def is_armstrong_number(number):
    if number < 0:
        return False

    length = len(str(number))

    numbersum = sum(int(dight) ** length for dight in str(number))

    return number == numbersum