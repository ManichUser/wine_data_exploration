import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # 1. Chargement  du  dataset
    df = pd.read_csv("../data/wine/wine.data", header=None)

    #  ajout des colonnes pour mieux les comprendre
    df.columns = [
        "Classe", "Alcohol", "Malicacid", "Ash", "Alcalinity_of_ash", "Magnesium",
        "Total_phenols", "Flavanoids", "Nonflavanoid_phenols", "Proanthocyanins",
        "Color_intensity", "Hue", "0D280_0D315_of_diluted_wines", "Proline"
    ]

    print("Aperçu des 20 premiere lignes :")
    print(df.head(20), "\n")

    #   histogramme de l'alcool
    plt.figure(figsize=(8, 5))
    plt.hist(df["Alcohol"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Histogramme de l'Alcohol")
    plt.xlabel("Teneur en alcool")
    plt.ylabel("Fréquence")
    plt.show()

    # 4. Tracer un boxplot : distribution de l'alcool selon la classe
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="Classe", y="Alcohol", data=df, palette="Set2")
    plt.title("Boxplot de l'Alcohol par Classe de vin")
    plt.show()

    # 5. Heatmap des corrélations
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=False, cmap="coolwarm")
    plt.title("Heatmap des corrélations")
    plt.show()


if __name__ == "__main__":
    main()
