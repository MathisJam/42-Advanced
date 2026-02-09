class calculator:

    def __init__(self, vector):
        '''Calculator constructor'''
        self.vector = vector

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Le total des 2 sequences de nombres'''
        try:
            assert len(V1) == len(V2), "Vectors must have the same length"
            dot_product = 0
            for i in range(len(V1)):
                dot_product += V1[i] * V2[i]
            print(f"Dot product is : {dot_product}")
        except Exception as err:
            print(f"Error: {err}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''Additionne les elements des deux vecteurs'''
        v = [float(sum(x)) for x in zip(V1, V2)]
        print(f"Add vector is : {v}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''Soustrait les elements des deux vecteurs'''
        v = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous vector is : {v}")

# ========= TESTTTTTTT =========
# def main():
#     a = [5, 10, 2]
#     b = [2, 4, 3]
#     calculator.dotproduct(a,b)
#     calculator.add_vec(a,b)
#     calculator.sous_vec(a,b)

# if __name__ == "__main__":
#     main()
