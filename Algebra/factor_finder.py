# The brief: You learned about the factor() function, which prints the factors of an expression.
# Now that you know how your program can handle expressions input by a user,
# write a program that will ask the user to input an expression, calculate its factors, and print them.
# Your program should be able to handle invalid input by making use of exception handling.
# Programming Challenge #1 of Amit Saha's 'Doing Maths with Python' Chapter 4

from sympy import sympify, factor, SympifyError


def factoriser(expr):
    return factor(expr)

if __name__=='__main__':
    expr = input('Enter your expression: ')

    try:
        factored_expr = sympify(expr)

    except SympifyError:
        print('Invalid expression')
    else:
        print(factoriser(factored_expr))
