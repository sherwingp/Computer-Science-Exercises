## Sherwin's Project Euler Explanations

# Problem 1 - Multiples of 3 and 5:

A for loop was used iterating to 1000. If variable i mod 3 or 5 equated to 0, it was added to the sum x.

# Problem 2 - Even Fibonacci numbers:

Variables a and b were initiated at 0 and 1 as the first two previous terms. X was initiated at 0 as the sum counter.
A for loop was created to iterate from 2 to 4 million.

For each iteration the previous two terms (a + b) were added together and held in variable c.
Variable a became the lower previous term (b), and b became the higher previous term (c).
If b (the higher term) mod 0 equated to 2 it was even, so it was added to the sum x.
After sum x exceeded 4 million the loop was broken, and sum x was printed.

# Problem 3 - Largest prime factor:

After looking up prime factors on the internet I found that a prime factor could not be more than the square root of a number.
Therefore, I created a loop iterating from the square root of the number down to 3.
For each iteration it checks if it is a factor using modulo. 
Then a nested loop checks if it is a prime, again using modulo.

# Problem 4 - Largest palindrome product:
First, I created a loop and another nested loop iterating from 999 to 1. 
Then, I multiplied the counters together and used variable k to hold the value. 
I checked if that was a palindrome by converting it to a string and using a slice that step backwards.

https://www.w3schools.com/python/python_howto_reverse_string.asp
Lastly, the biggest palindrome was contained in biggest palindrome and then printed at the end of the loop.
