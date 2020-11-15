'''
Statistics calculator

This is a programming challenge from 'Doing Math with Python' ch. 3
Implement a statistics calculator that takes a list of numbers in the file mydata.txt and then calculates and prints their mean, median, mode, variance, and standard deviation.
'''

from collections import Counter

def calculate_mean(numbers):
    s = sum(numbers)
    n = len(numbers)

    # Calculate the mean
    mean = s/n

    return mean

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

def calculate_mode(numbers):

    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes

def find_differences(numbers):
    diff = []
    for num in numbers:
        diff.append(num - mean)
    return diff

def calculate_variance(numbers):

    # Find the list of differences
    diff = find_differences(numbers)

    # Find the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)

    # Find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff / len(numbers)
    return variance

if __name__ == '__main__':

    with open('mydata.txt', 'r') as f:
        list = [int(x) for x in f.read().split()]

    modes = calculate_mode(list)
    median = calculate_median(list)
    mean = calculate_mean(list)
    variance = calculate_variance(list)

    print('The mean is {0}'.format(mean))
    print('The median is {0}'.format(median))
    print('The modes of the list are: ')
    for mode in modes:
        print(mode)
    print('The variance of the list of numbers is {0}'.format(variance))
    std = variance**0.5
    print('The standard deviation of the list of numbers if {0}'.format(std))