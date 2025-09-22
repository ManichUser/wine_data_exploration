import pandas as pd

# Charger les datasets
red_wine = pd.read_csv("winequality-red.csv", sep=";")
white_wine = pd.read_csv("winequality-white.csv", sep=";")

# Ajout  colonne type de vin
red_wine["type"] = "red"
white_wine["type"] = "white"

# Fusion des deux datasets
wine_data = pd.concat([red_wine, white_wine], ignore_index=True)

# Affichage des 5 premières lignes
print(wine_data.head())

