# Doing Math with Python Ch. 1 Programming Challenge #4: Fraction Calculator

from fractions import Fraction

def add(a, b):
    print('Result of Addition: {0}'.format(a+b))

def subtract(a, b):
    print('Result of Subtraction: {0}'.format(a-b))

def divide(a, b):
    print('Result of Division: {0}'.format(a/b))

def multiply(a, b):
    print('Result of Multiplication: {0}'.format(a*b))

if __name__ == '__main__':

    while True:

        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
        op = op.lower()

        if op == 'add':
            add(a, b)
        if op == 'subtract':
            subtract(a, b)
        if op == 'divide':
            divide(a, b)
        if op == 'multiply':
            multiply(a, b)

        answer = input('Do you want to exit? (y) for yes ')
        if answer.lower() == 'y':
            break
