'''
Calculating the mode

Example from 'Doing Math with Python' ch. 3
Changed to add user input
List input code from https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
'''

from collections import Counter

def calculate_mode(numbers):

    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes

if __name__ == '__main__':
    list = []
    n = int(input('Enter number of elements: '))

    for i in range(0, n):
        elements = int(input())

        list.append(elements)

    modes = calculate_mode(list)

    print('The modes of the list are: ')
    for mode in modes:
        print(mode)