import os
os.system('clear')

TTMC = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '...-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

MCTT = {}
for key, value in TTMC.items():
    MCTT[value] = key


def text_to_morse():
    string_to_convert = input("Enter a string that you would like to convert to Morse Code:\n")
    morse_code = ""

    for char in string_to_convert:
        if char.upper() in TTMC:
            morse_code += TTMC[char.upper()] + ' '
        elif char.isspace():
            morse_code += '   '

    print(f"\nThe Morse Code for the inputted String is:\n{morse_code}")


def morse_to_text():
    string_to_convert = input("Follow the below rules while entering the Morse Code:\n"
                              "1. Each word should be separated by 3 spaces mandatorily.\n"
                              "2. Each letter inside a word should be separated by 1 space.\n"
                              "Enter the Morse Code that you would like to convert to text:\n")
    plain_text = ""
    words = string_to_convert.split('   ')

    for word in words:
        chars = word.split()
        for char in chars:
            plain_text += MCTT[char]
        plain_text += ' '

    print(f"The plain text equivalent for the inputted Morse Code is:\n{plain_text}")


print("TEXT TO MORSE CODE AND MORSE CODE TO TEXT CONVERTER")
converter = int(input("What would you like to do? (Enter 1 or 2)\n"
                      "1. Text to Morse Code\n"
                      "2. Morse Code to Text\n"))

if converter == 1:
    text_to_morse()
elif converter == 2:
    morse_to_text()
else:
    print("Invalid input!! Exiting...")
