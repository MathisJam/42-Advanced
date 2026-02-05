from load_csv import load
import matplotlib.pyplot as plt


def all_life():
    '''Charge un DataFrame et affiche les informations
    du pays choisi (ici, France)
    - on trouve la ligne ou country == france
    - on transpose index et columns
    toutes les annees qui etaient dans les cols de France
    sont maintenant ses index, et on peut faire un graph avec'''
    try:
        df = load('life_expectancy_years.csv')
        assert df is not None, "Load function returned none"

        fr_df = df.loc[df['country'] == 'France']
        fr_df = fr_df.drop(columns="country").T

        fr_df.plot(legend=False)
        plt.xlabel("Years")
        plt.ylabel("Life expectancy")
        plt.title("France life expectancy Projections")
        plt.show()
    except Exception as error:
        print(f"Error: {error}")
        return


def main():
    try:
        all_life()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: interruption signal caught")


if __name__ == "__main__":
    main()
