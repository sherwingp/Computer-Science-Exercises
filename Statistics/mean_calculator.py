'''
Calculating the mean

Adapted from 'Doing Math with Python' ch. 3
Changed to add user input
List input code from https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
'''

def calculate_mean(numbers):
    s = sum(numbers)

    # Calculate the mean
    mean = s/n

    return mean

if __name__ == '__main__':
    list = []
    n = int(input('Enter number of elements: '))

    for i in range(0, n):
        elements = int(input())

        list.append(elements)
    mean = calculate_mean(list)

    print('The mean is {0}'.format(mean))
