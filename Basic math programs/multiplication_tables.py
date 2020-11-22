# Doing Math With Python Ch 1 Programming Challenge #2: Enhanced Multiplication Table Generator

def multi_table(a, b):
    for i in range(1, b+1):
        print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':

    while True:
        a = input('Enter a number: ')
        b = input('Up to which multiple? ')
        multi_table(float(a), int(b))

        answer = input('Do you want to exit? (y) for yes ')
        if answer.lower() == 'y':
            break
