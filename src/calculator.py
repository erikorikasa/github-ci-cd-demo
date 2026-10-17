def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulo(a, b):
    return a % b


def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    guess = x
    for _ in range(20):
        if guess == 0:
            break
        guess = (guess + x / guess) / 2
    return guess
