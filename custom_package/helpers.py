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


def log_execution_time(func):
    import time

    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Execution time:", end_time - start_time, "seconds")

    return wrapper
