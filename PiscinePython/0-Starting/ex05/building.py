import sys


def building():
    """Compte les diff categories de caracteres dans un texte"""
    try:
        assert len(sys.argv) <= 2, "more than one argument are provided"
        if len(sys.argv) == 2:
            text = sys.argv[1]
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return

    if len(sys.argv) != 2:
        text = input("What is the text to count?\n") + "\n"

    Nb_Char = len(text)
    Nb_Upper = sum(1 for x in text if x.isupper())
    Nb_Lower = sum(1 for x in text if x.islower())
    Nb_Punct = sum(1 for x in text if x in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}")
    Nb_Space = sum(1 for x in text if x.isspace())
    Nb_Digit = sum(1 for x in text if x.isdigit())

    print(f"The text contains {Nb_Char} characters:")
    print(f"{Nb_Upper} upper letters")
    print(f"{Nb_Lower} lower letters")
    print(f"{Nb_Punct} punctuation marks")
    print(f"{Nb_Space} spaces")
    print(f"{Nb_Digit} digits")


def main():
    building()


if __name__ == "__main__":
    main()
