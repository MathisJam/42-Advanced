import sys


def toMorse(string):
    MORSE_DICT = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        " ": "/ ",
    }

    morse_string = ""
    for char in string:
        morse_string += MORSE_DICT[char.upper()] + " "

    return morse_string


def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    message = sys.argv[1]

    if not message or not all(c.isalnum() or c.isspace() for c in message):
        print("AssertionError: the arguments are bad")
        return

    morse_message = toMorse(message)
    print(morse_message)


main()
