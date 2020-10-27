'''
This program finds the sum of an arbitrary series when you supply the nth term of the series
and the number of terms in it.
'''

from sympy import sympify, Symbol, summation, pprint

def sum_series(nth_term, terms, n):
    s = summation(nth_term, (n, 1, terms))
    pprint(s)

if __name__ == '__main__':
    nth_term = sympify(input('Enter the nth term: '))
    n = Symbol('n')
    terms = int(input('Enter the number of terms you want in the series: '))

    sum_series(nth_term, terms, n)