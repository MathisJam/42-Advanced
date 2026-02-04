def ft_filter(function, iterable):
    """Applique une fonction sur chaque element dun iterable
    et retourne une liste des elements pour lesquels"""
    try:
        if function:
            return [item for item in iterable if function(item)]
    except Exception:
        return []
    return [item for item in iterable if item]


# ======== TESTTTT =========
# def starts_a(w):
#     """retourne si le mot commence par a"""
#     return w.startswith("a")


# def main():
#     li = ["apple", "banana", "avocado", "cherry", "apricot"]
#     res = ft_filter(starts_a, li)
#     print(list(res))


# if __name__ == "__main__":
#     main()
