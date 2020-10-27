'''
Write a program that asks the user for two expressions and then graphs them both
'''

from sympy import Symbol, sympify, solve, SympifyError
from sympy.plotting import plot

def solver(expr1, expr2, x, y):
    soln = solve((expr1, expr2), dict=True)

    if soln:
        # Prints solution
        print('x = {0}, y = {1}'.format(soln[0][x], soln[0][y]))

        # Plots equations
        expr1_y = solve(expr1, 'y')[0]
        expr2_y = solve(expr2, 'y')[0]
        p = plot(expr1_y, expr2_y, legend=True, show=False)
        p[0].line_color = 'b'
        p[1].line_color = 'r'
        p.show()

    else:
        print('No solution found.')

if __name__=='__main__':

    expr1 = input('Enter your first expression in terms of x and y: ')
    expr2 = input('Enter your second expression in terms of x and y: ')

try:
    expr1 = sympify(expr1)
    expr2 = sympify(expr2)

except SympifyError:
    print('Invalid input')
else:
    x = Symbol('x')
    y = Symbol('y')
    solver(expr1, expr2, x, y)

