from ft_filter import ft_filter


def starts_a(w):
    return w.startswith("a")


def main():
    li = ["apple", "banana", "avocado", "cherry", "apricot"]
    res = ft_filter(starts_a, li)
    print(list(res))


main()
