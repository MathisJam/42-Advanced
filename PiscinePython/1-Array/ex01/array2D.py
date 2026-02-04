def slice_me(family: list, start: int, end: int) -> list:
    """Retourne la nouvelle liste a partir de la liste family
    on la coupe de start jusqu'a end (non inclus)"""
    try:
        assert len(family) > 0, "Family list must not be empty"
        assert type(family) is list, "Family must be of type list"
        assert len(set(map(len, family))) == 1, "Lists must be of same size"
        if end < 0:
            end = end * -1
        nb_in = len(family[0])
        print(f"My shape is : ({len(family)}, {nb_in})")
        sliced = family[start:end]
        print(f"My new shape is : ({len(sliced)}, {nb_in})")

        return family[start:end]
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return
    except Exception as error:
        print(f"Unexpected error: {error}")
        return


# =========== TESSSSSSSTTTTTTTTTTSSSSSSSS ===============
# def main():
#     from array2D import slice_me

#     family = [[]]
#     print(slice_me(family, 0, 2))
#     print(slice_me(family, 1, -2))

# if __name__ == "__main__":
#     main()
