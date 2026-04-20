import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_distributions(df: pd.DataFrame) -> None:
    sns.histplot(df["points"], bins=20)
    plt.title("Distribution of Wine Ratings")
    plt.show()

    sns.histplot(df["price"], bins=50)
    plt.title("Price Distribution")
    plt.show()


def plot_country_counts(df: pd.DataFrame) -> None:
    top_countries = df["country"].value_counts().head(10)
    top_countries.plot(kind="bar")
    plt.title("Top Wine Producing Countries")
    plt.show()


def plot_relationships(df: pd.DataFrame) -> None:
    sns.scatterplot(x="price", y="points", data=df)
    plt.title("Price vs Rating")
    plt.show()


def plot_correlation(df: pd.DataFrame) -> None:
    correlation = df[["price", "points"]].corr()
    sns.heatmap(correlation, annot=True)
    plt.title("Correlation Matrix")
    plt.show()


def plot_price_category(df: pd.DataFrame) -> None:
    df["price_category"].value_counts().plot(kind="bar")
    plt.title("Wine Price Categories")
    plt.show()
