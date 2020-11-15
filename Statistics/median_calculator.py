'''
Calculating the median

Example from 'Doing Math with Python' ch. 3
Changed to add user input of a list of numbers
List input code from https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
'''

def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()

    # Find the median
    if N % 2 == 0:
        m1 = N/2
        m2 = (N/2) + 1

        # Convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) -1
        median = (numbers[m1] + numbers[m2]) / 2

    else:
        m = (N+1) / 2

        # Convert to integer, match position
        m = int(m) - 1
        median = numbers[m]

    return median

if __name__ == '__main__':
    list = []
    n = int(input('Enter number of elements: '))

    for i in range(0, n):
        elements = int(input())

        list.append(elements)
    median = calculate_median(list)

    print('The median is {0}'.format(median))
