'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt

n = input('Enter a number: ')
n = int(n)

for i in range(int(sqrt(n)), 3, -1):

# Check if factor
    if n % i == 0:

# Check for prime
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


