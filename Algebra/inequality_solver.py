'''
This programme solves inequalities
'''

from sympy import sympify, SympifyError, Symbol
from sympy import solve_poly_inequality, solve_rational_inequalities, solve_univariate_inequality, Poly

def isolve(ineq_object):

    x = Symbol('x')
    expr = ineq_object.lhs
    rel = ineq_object.rel_op

    # Solves polynomial inequalities
    if expr.is_polynomial():
        p = Poly(expr, x)
        return solve_poly_inequality(p, rel)

    # Solves rational inequalities
    elif expr.is_rational_function():
        numer, denom = expr.as_number_denom()
        p1 = Poly(numer)
        p2 = Poly(denom)
        return solve_rational_inequalities([[((p1, p2), rel)]])

    # Solves univariate inequalities
    else:
        return solve_univariate_inequality(ineq_object, x, relational=False)

if __name__ =='__main__':
    ineq = input('Enter the inequality to be solved: ')
    try:
        ineq_object = sympify(ineq)
    except SympifyError:
        print('Invalid inequality')
    else:
        print(isolve(ineq_object))