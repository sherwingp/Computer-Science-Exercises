'''
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

biggest_palindrome = 0

# Iterates from 999 to 1
for i in range(999, 1, -1):
    for j in range(999, 1, -1):
        k = i * j
        reverse_k = str(k)[::-1]

        # Reverses and checks if palindrome
        if str(k) == reverse_k:
            palindrome = k
            
            # Checks if biggest palindrome
            if palindrome > biggest_palindrome:
                biggest_palindrome = palindrome

print(biggest_palindrome)

