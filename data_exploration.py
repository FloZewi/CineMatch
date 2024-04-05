import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def explore_data(df, df_name):
    """Druckt grundlegende Informationen über einen DataFrame."""
    print(f"Exploring {df_name}:")
    print(f"Shape: {df.shape}")
    print("First 5 rows:")
    print(df.head())
    print("\nBasic statistics:")
    print(df.describe())
    print("\n")
    """Druckt grundlegende Informationen über einen DataFrame."""
    print(f"Exploring {df_name}:")
    print(f"Shape: {df.shape}")
    print("First 5 rows:")
    print(df.head())
    print("\nBasic statistics:")
    print(df.describe())
    print("\n")


def basic_statistics(df):
    """Druckt grundlegende Informationen für numerische Spalten eines DataFrame."""
    print(df.describe())


def plot_distributions(df, numeric_columns=None, categorical_columns=None):
    """Plottet Verteilungen für gegebene Spalten."""
    for col in numeric_columns:
        plt.figure(figsize=(10, 4))
        sns.histplot(df[col], kde=True)
        plt.title(f'Verteilung von {col}')
        plt.show()

    for col in categorical_columns:
        plt.figure(figsize=(10, 4))
        sns.countplot(data=df, x=col)
        plt.title(f'Häufigkeitsverteilung von {col}')
        plt.show()


def missing_data(df):
    """Zeigt den Prozentsatz der fehlenden Daten pro Spalte."""
    missing = df.isnull().mean() * 100
    missing = missing[missing > 0]
    print("Prozentsatz der fehlenden Daten pro Spalte:")
    print(missing)


def correlation_heatmap(df):
    """Zeigt die Korrelationsmatrix für numerische Spalten."""
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.show()


def plot_histograms(df, columns):
    for col in columns:
        plt.figure(figsize=(10, 4))
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot von {col}')
        plt.show()


def load_csv_file(file_path):
    """ Lädt eine CSV-Datei und gibt einen DataFrame zurück. """
    return pd.read_csv(file_path)


def load_datasets():
    """Lädt alle erforderlichen Datensätze und gibt sie zurück."""
    movies_df = load_csv_file("movies.csv")
    ratings_df = load_csv_file("ratings.csv")
    return movies_df, ratings_df


def main():
    # Laden der Datensätze
    movies_df, ratings_df = load_datasets()

    # Exploration der Daten
    explore_data(movies_df, ratings_df)

    # Überprüfen der Spaltennamen in movies_df
    print("Spalten in movies_df:", movies_df.columns)

    # Ausgabe der ersten fünf Zeilen des movies DataFrame
    print("Erste Zeilen von movies_df:")
    print(movies_df.head())

    # Basisstatistiken anzeigen
    basic_statistics(movies_df)

    # Fehlende Daten anzeigen
    missing_data(movies_df)

    # Korrelationen anzeigen
    correlation_heatmap(ratings_df)

    # Histogramm plotten
    print("Überprüfung der Spalte 'title' in movies_df:")
    print(movies_df['title'].head())


if __name__ == "__main__":
    main()
