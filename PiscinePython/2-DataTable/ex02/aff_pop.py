from load_csv import load
import matplotlib.pyplot as plt


def aff_pop():
    '''Charge un DataFrame et affiche les informations
    des pays choisi (ici, France, Allemagne)
    - on trouve la ligne ou country == france/allemagne
    - on transpose index et columns
    - On passe les valeurs en float (en enlevant les M car convers. impossible)
    toutes les annees qui etaient dans leurs columns
    sont maintenant leurs index, et on peut faire un graph avec'''
    try:
        df = load('population_total.csv')
        assert df is not None, "Load function returned none"

        fr_df = df.loc[df['country'] == 'France']
        fr_df = fr_df.drop(columns="country").T

        ge_df = df.loc[df['country'] == 'Germany']
        ge_df = ge_df.drop(columns="country").T

        fr_df.columns = ['France']
        ge_df.columns = ['Germany']

        years = [int(x) for x in fr_df.index]
        fr_values = [float(x.replace('M', '')) for x in fr_df['France']]
        ge_values = [float(x.replace('M', '')) for x in ge_df['Germany']]

        filtered = [(y, f, g) for y, f, g, in zip(
            years, fr_values, ge_values) if y >= 1800 and y <= 2050]
        if filtered:
            years, fr_values, ge_values = zip(*filtered)

        plt.plot(years, fr_values, label='France')
        plt.plot(years, ge_values, label='Germany')
        plt.xlabel("Years")
        plt.ylabel("Population in M")
        plt.title("Population Projections")
        plt.show()
    except Exception as error:
        print(f"Error: {error}")
        return


def main():
    try:
        aff_pop()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: interruption signal caught")


if __name__ == "__main__":
    main()
