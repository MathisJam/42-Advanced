from typing import Any


def callLimit(limit: int):
    count = 0
    value = limit

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
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
