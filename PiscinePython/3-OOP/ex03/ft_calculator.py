class calculator:

    def __init__(self, vector):
        '''Calculator constructor'''
        self.vector = vector

    def __add__(self, object) -> None:
        '''Additionne la valeur donnee a chaque elems du vector'''
        vec2 = [i+object for i in self.vector]
        print(vec2)
        self.vector = vec2

    def __mul__(self, object) -> None:
        '''Multiplie la valeur donnee aux elems du vector'''
        vec2 = [i*object for i in self.vector]
        print(vec2)
        self.vector = vec2

    def __sub__(self, object) -> None:
        '''Soustrait la valeur donnee aux elems du vector'''
        vec2 = [i-object for i in self.vector]
        print(vec2)
        self.vector = vec2

    def __truediv__(self, object) -> None:
        '''Divise la valeur donnee aux elems du vector'''
        try:
            vec2 = [i/object for i in self.vector]
        except ZeroDivisionError:
            return print("ZeroDivisionError: Unauthorized division by zero")
        print(vec2)
        self.vector = vec2

# ========= TESTTTTTTTT =========
# def main():
#     v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
#     v1 + 5
#     print("---")
#     v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
#     v2 * 5
#     print("---")
#     v3 = calculator([10.0, 15.0, 20.0])
#     v3 - 5
#     v3 / 5

# if __name__ == "__main__":
#     main()
