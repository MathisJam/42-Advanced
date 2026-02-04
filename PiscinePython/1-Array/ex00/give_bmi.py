def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """Calcul l'IMC (BMI) a partir de la taille et du poids.
    IMC = poids / taille, on multiplie la taille pour avoir en metre"""
    try:
        assert len(height) > 0 and len(weight) > 0, "Lists must not be empty"
        bmi = [w / (h * h) for h, w in zip(height, weight)]
        return bmi
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Applique une limite a la liste d'IMC (BMI), retourne true si superieur
    a la limite, sinon false"""
    try:
        assert len(bmi) > 0, "BMI list must not be empty"
        limited_bmi = [b > limit for b in bmi]
        return limited_bmi
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return []

# ============== TEEEEEEEEEEEEEEEESSSSSSSSSSSSSTTTTTTTTTTTSSSSSSS =============
# def main():
#     height = [2.71, 1.15]
#     weight = [165.3, 38.4]
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))

# if __name__ == "__main__":
#     main()
