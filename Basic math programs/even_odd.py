def odd_even(number):
    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')

    for i in range(number, number+19, 2):
        print(i)

if __name__ == '__main__':

    while True:

        number = input('Enter a number: ')
        number = float(number)

        if number > 0 and number.is_integer():
            odd_even(int(number))
        else:
            print('Please enter a positive integer')

        answer = input('Do you want to exit? (y) for yes ')
        if answer.lower() == 'y':
            break