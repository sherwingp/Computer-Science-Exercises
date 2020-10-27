# Unit converter: Miles and kilometres

def print_menu():
    print('1. Kilometres to Miles')
    print('2. Miles to Kilometres')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')
    print('5. Celsius to Fahrenheit')
    print('6. Fahrenheit to Celsius')

def km_miles():
    km = float(input('Enter distance in kilometres: '))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609

    print('Distance in kilometres: {0}'.format(km))

def kg_lb():
    kg = float(input('Enter weight in kilograms: '))
    lb = kg * 2.2046226218

    print('Weight in pounds: {0}'.format(lb))

def lb_kg():
    lb = float(input('Enter weight in pounds: '))
    kg = lb / 2.2046226218

    print('Weight in kilograms: {0}'.format(kg))

def c_f():
    c = float(input('Enter temperature in celsius'))
    f = c * 9/5 + 32

    print('Temperature in fahrenheit: {0}'.format(f))

def f_c():
    f = float(input('Enter temperature in fahrenheit: '))
    c = round((f - 32) * 5/9)

    print('Temperature in celsius: {0}'.format(c))

if __name__ == '__main__':

        while True:

            print_menu()
            choice = input('Which conversion would you like to do?: ')
            if choice == '1':
                km_miles()
            if choice == '2':
                miles_km()
            if choice == '3':
                kg_lb()
            if choice == '4':
                lb_kg()
            if choice == '5':
                c_f()
            if choice == '6':
                f_c()

            answer = input('Do you want to exit? (y) for yes ')
            if answer.lower() == 'y':
                break