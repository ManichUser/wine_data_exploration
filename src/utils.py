import seaborn as sns
import matplotlib.pyplot as plt

def plot_hist(df, col, bins=20):
    plt.figure(figsize=(8,5))
    sns.histplot(df[col], bins=bins, kde=True)
    plt.title(f"Distribution de {col}")
    plt.show()

def plot_corr(df):
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Matrice de corrélation")
    plt.show()
