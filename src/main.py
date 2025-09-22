# main.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
red_wine = pd.read_csv("../data/winequality-red.csv", sep=";")
white_wine = pd.read_csv("../data/winequality-white.csv", sep=";")

# Ajouter une colonne pour distinguer les types
red_wine["type"] = "red"
white_wine["type"] = "white"

# Fusionner les deux datasets
wine_data = pd.concat([red_wine, white_wine], ignore_index=True)

def plot_hist(df, col, bins=20, with_type=False):
    plt.figure(figsize=(8,5))
    if with_type:
        sns.histplot(data=df, x=col, bins=bins, kde=True, hue="type", alpha=0.5)
    else:
        sns.histplot(df[col], bins=bins, kde=True)
    plt.title(f"Distribution de {col}")
    plt.show()

def plot_corr(df):
    plt.figure(figsize=(10,8))
    # Supprimer "type" qui est non numérique
    sns.heatmap(df.drop(columns=["type"]).corr(), annot=True, cmap="coolwarm")
    plt.title("Matrice de corrélation")
    plt.show()


if __name__ == "__main__":
    #  distribution de l'alcool
    plot_hist(wine_data, "alcohol", bins=30, with_type=True)

    # distribution de l’acidité volatile
    plot_hist(wine_data, "volatile acidity", bins=30, with_type=True)

    # Matrice de corrélation
    plot_corr(wine_data)
