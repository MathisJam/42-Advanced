import sys
from ft_filter import ft_filter


def main():
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    string = sys.argv[1]

    if string == "":
        print("AssertionError: the arguments are bad")
        return

    try:
        n = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    result = ft_filter(lambda word: len(word) > n, string.split())
    print(result)


main()
