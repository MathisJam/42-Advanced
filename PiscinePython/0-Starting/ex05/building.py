import sys


def building():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
        exit()

    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        text = input("What is the text to count?\n") + "\n"

    Nb_Char = len(text)
    print(f"The text contains {Nb_Char} characters:")

    Nb_Upper = sum(1 for x in text if x.isupper())
    print(f"{Nb_Upper} upper letters")

    Nb_Lower = sum(1 for x in text if x.islower())
    print(f"{Nb_Lower} lower letters")

    Nb_Punct = sum(1 for x in text if x in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}")
    print(f"{Nb_Punct} punctuation marks")

    Nb_Space = sum(1 for x in text if x.isspace())
    print(f"{Nb_Space} spaces")

    Nb_Digit = sum(1 for x in text if x.isdigit())
    print(f"{Nb_Digit} digits")


def main():
    building()


main()
