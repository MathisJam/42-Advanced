import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''Ecrit les dimensions du data set
    donne en argument (le path -> dataset)'''

    try:
        assert path != "", "Path must not be null"
        assert path.lower().endswith(".csv"), "File must be in format .csv"

        # On peut fait plus lisible en mettant les options en commentaire
        # Mais on verra pas toutes les lignes
        pd.set_option("display.max_rows", None)
        pd.set_option("display.min_rows", None)

        df = pd.read_csv(path)
        assert df is not None, "File doesn't exist"
        print(f"Loading dataset of dimensions {df.shape}")

        return df
    except Exception as error:
        print(f"Error: {error}")
        return None

# =========== TESTTTTTSSSSSSSSS =========
# def main():
#         print(load("life_expectancy_years.csv"))

# if __name__ == "__main__":
#     main()
