from typing import Any


def callLimit(limit: int):
    '''Fonction mere qui encapsule les autres
    et qui recupere la limite'''
    count = 0
    value = limit

    def callLimiter(function):
        '''Fonction qui permet d'encapsuler
        limit_function et recuperer la function'''
        def limit_function(*args: Any, **kwds: Any):
            '''Fonction encapsulee qui regarde si
            la limite d'appel a ete depassee'''
            nonlocal count
            try:
                assert count < value, "call too many times"
            except Exception as err:
                print(f"Error: {function} {err}")
                return
            count += 1
            return function(*args, **kwds)
        return limit_function
    return callLimiter

# ======== TESTSSSSSSS =================
# def main():
#     '''Doc nulle pour norme'''


# @callLimit(3)
# def f():
#     print("f()")


# @callLimit(1)
# def g():
#     print("g()")


# for i in range(3):
#     f()
#     g()

# if __name__ == "__main__":
#     main()
