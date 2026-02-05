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
        try:
            df = pd.read_csv(path)
        except FileNotFoundError:
            print(f"FileNotFoundError: File {path} doesn't exist")
            return None
        assert df is not None, "File doesn't exist"

        return df
    except Exception as error:
        print(f"Error: {error}")
        return None
