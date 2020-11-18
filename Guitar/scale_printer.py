# This program is based on Diego Penilla's 'Learn Guitar with Python'
# https://medium.com/better-programming/how-to-learn-guitar-with-python-978a1896a47
# Adapting the code, I created a program that prints out the user-inputted scale.

def print_menu():
    print('1. Major')
    print('2. Minor')
    print('3. Dorian')
    print('4. Phrygian')
    print('5. Minor Pentatonic')
    print('6. Major Pentatonic')
    print('7. Harmonic Minor')
    print('8. Mixolydian')
    print('9. Minor Blues')
    print('10. Locrian')
    print('11. Lydian')

scales = {
    "1": [0, 2, 4, 5, 7, 9, 11],
    "2": [0, 2, 3, 5, 7, 8, 10],
    "3": [0, 2, 3, 5, 7, 9, 10],
    "4": [0, 1, 3, 5, 7, 8, 10],
    "5": [0, 3, 5, 7, 10],
    "6": [0, 2, 4, 7, 9],
    "7": [0, 2, 3, 5, 7, 8, 11],
    "8": [0, 2, 4, 5, 7, 9, 10],
    "9": [0, 2, 3, 5, 6, 7, 10],
    "10": [0, 1, 3, 5, 6, 8, 10],
    "11": [0, 2, 4, 6, 7, 9, 11],
}

def get_notes(key, intervals):
    # a sufficiently long sequence of notes to slice from
    whole_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] * 3
    # finding start of slice
    root = whole_notes.index(key)
    # taking 12 consecutive elements
    octave = whole_notes[root:root+12]
    # accessing indexes specified by `intervals` to retrieve notes
    return [octave[i] for i in intervals]

if __name__ == '__main__':

    root = input('Enter the root: ')
    print_menu()
    scale = input('Enter the scale: ')

    user_scale = scales[scale]

    output_scale = get_notes(root, user_scale)

    print(output_scale)
