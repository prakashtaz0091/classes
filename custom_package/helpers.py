def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def factorial(number):
    for i in range(1, number):
        number *= i
    return number
