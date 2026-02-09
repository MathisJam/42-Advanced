def square(x: int | float) -> int | float:
    '''Retourne le nombre au carre'''
    return x * x


def pow(x: int | float) -> int | float:
    '''Retourne le nombre puissance nombre'''
    return x ** x


def outer(x: int | float, function) -> object:
    '''Prend un nombre et une fonction,
    retourne un objet qui une fois appele
    donne le resultat du nombre apres la fonction'''
    value = x
    count = 0

    def inner() -> float:
        '''Accede aux variables de outer et les modifie
        '''
        nonlocal value, count
        value = function(value)
        count += 1
        return value
    return inner

# =========== TESTTTTTTTTTSSSSSSS ============
# def main():
#     my_counter = outer(3, square)
#     print(my_counter())
#     print(my_counter())
#     print(my_counter())
#     print("---")
#     another_counter = outer(1.5, pow)
#     print(another_counter())
#     print(another_counter())
#     print(another_counter())

# if __name__ == "__main__":
#     main()
