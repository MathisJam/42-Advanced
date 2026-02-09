from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    '''Prend un nombre indefini d'arguments et fait
    la moyenne, la medianne, le quartile inferieur et superieur,
    ainsi que l'ecart type et la variance, en fonction de
    ce que **kwargs exige.'''
    try:
        assert len(args) > 0, "ERROR"
        assert len(kwargs) > 0, "ERROR"

        values = [v.lower() for v in kwargs.values()]
        valid = {'mean', 'median', 'quartile', 'std', 'var'}

        assert any(v in valid for v in values), "ERROR"

        if 'std' in values:
            mean = sum(args) / len(args)
            dev = [(x - mean) ** 2 for x in args]
            var = sum(dev) / len(args)
            std = var ** 0.5
            print(f"std : {std}")

        if 'mean' in values:
            print(f"mean : {sum(args) / len(args)}")

        if 'var' in values:
            mean = sum(args) / len(args)
            dev = [(x - mean) ** 2 for x in args]
            var = sum(dev) / len(args)
            print(f"var : {var}")

        if 'median' in values:
            sorted_nums = sorted(args)
            mid = len(args) // 2
            if len(args) % 2 == 1:
                median = sorted_nums[mid]
            else:
                median = (sorted_nums[mid] + sorted_nums[mid - 1]) / 2
            print(f"median : {median}")

        if 'quartile' in values:
            sorted_nums = sorted(args)
            mid = len(args) // 2
            lower_half = sorted_nums[:mid + 1]
            upper_half = sorted_nums[mid:]

            l1 = len(lower_half)
            mid_l = l1 // 2
            if l1 % 2 == 1:
                Q1 = float(lower_half[mid_l])
            else:
                Q1 = float((lower_half[mid_l] + lower_half[mid_l - 1]) / 2)

            l2 = len(upper_half)
            mid_l2 = l2 // 2
            if l2 % 2 == 1:
                Q3 = float(upper_half[mid_l2])
            else:
                Q3 = float((upper_half[mid_l2] + upper_half[mid_l2 - 1]) / 2)
            print(f"quartile : [{Q1}, {Q3}]")

    except Exception as err:
        print(f"{err}")
        return


# =========== TESSSSSSSSSTTTTTTTTTTTSSSSSS ===========
# def main():
#     ft_statistics(1, 42, 360, 11, 64,
#                   toto="mean", tutu="median", tata="quartile")
#     print("-----")
#     ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
#                   hello="std", world="var")
#     print("-----")
#     ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
#                   ejfhhe="heheh", ejdjdejn="kdekem")
#     print("-----")
#     ft_statistics(toto="mean", tutu="median", tata="quartile")


# if __name__ == "__main__":
#     main()
