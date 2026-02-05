from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd


def format_k(x, pos):
    '''Convertit les valeurs >= 1000 en k'''
    if x >= 1000:
        return f"{int(x/1000)}k"
    else:
        return f"{int(x)}"


def projection_life():
    '''Charge 2 fichiers csv
    et affiche le graph de l'esperance de vie de la population
    en fonction du revenu brut de chaque pays en 1900
    - On recupere les columns country et 1900 pour savoir a quel
     pays correspond la valeur a 1900.
    - On fusionne le tout via country, nous creant une 3eme colonne
      [country | income | life], si un pays existe dans l'un des
      dataframe mais pas dans l'autre, il n'est pas ajoute.
    - On scatter (pour faire les petits points du graphique)
    en utilisant les valeurs des colonnes pour faire x/y
    - On change les ticks pour etre proche du sujet'''

    df_income = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life = load("life_expectancy_years.csv")

    income_1900 = df_income[['country', '1900']]
    life_1900 = df_life[['country', '1900']]

    res = pd.merge(income_1900, life_1900, on='country')
    res.columns = ['country', 'income_1900', 'life_1900']

    plt.scatter(res['income_1900'], res['life_1900'])
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectacy")
    plt.title("1900")

    plt.xscale("log")
    plt.xlim(300, 10000)

    ticks = [300, 1000, 10000]
    plt.gca().xaxis.set_major_locator(mticker.FixedLocator(ticks))
    plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(format_k))
    plt.show()


def main():
    try:
        projection_life()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: interruption signal caught")


if __name__ == "__main__":
    main()
