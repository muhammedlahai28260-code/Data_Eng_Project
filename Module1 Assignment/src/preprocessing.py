import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()

    df["price"] = df["price"].fillna(df["price"].median())
    df["country"] = df["country"].fillna("Unknown")
    df["province"] = df["province"].fillna("Unknown")

    return df


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df["price_category"] = pd.cut(
        df["price"],
        bins=[0, 20, 50, 100, 500],
        labels=["Cheap", "Affordable", "Expensive", "Luxury"],
    )
    return df
