import sys


def toMorse(string):
    """Transforme une string en code morse"""
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
        try:
            morse_string += MORSE_DICT[char.upper()] + " "
        except KeyError:
            print("AssertionError: the arguments are bad")
            return
    return morse_string


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        message = sys.argv[1]

        assert message and all(c.isalnum() or c.isspace() for c in message), (
            "the arguments are bad"
        )

    except AssertionError as error:
        print(f"AssertionError: {error}")
        return

    morse_message = toMorse(message)
    print(morse_message)


if __name__ == "__main__":
    main()
