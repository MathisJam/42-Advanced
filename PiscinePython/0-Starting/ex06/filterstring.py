import sys
from ft_filter import ft_filter


def main():
    """Filtre les mots d'une string selon leur longueur
    et affiche la liste des mots plus longs que n"""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        string = sys.argv[1]

        assert string != "", "the arguments are bad"
        n = int(sys.argv[2])

    except AssertionError as error:
        print(f"AssertionError: {error}")
        return
    except Exception:
        print("AssertionError: the arguments are bad")
        return

    result = ft_filter(lambda word: len(word) > n, string.split())
    print(result)


if __name__ == "__main__":
    main()
