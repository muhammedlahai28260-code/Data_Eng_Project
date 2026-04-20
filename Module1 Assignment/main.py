from src.data_loader import extract_zip, load_data
from src.preprocessing import clean_data, add_features
from src.visualization import (
    plot_distributions,
    plot_country_counts,
    plot_relationships,
    plot_correlation,
    plot_price_category
)
from src.utils import save_data


def main() -> None:
    # Step 1: Extract
    extract_zip("data/wine-reviews.zip", "data/")

    # Step 2: Load
    df = load_data(
        "data/winemag-data-130k-v2.csv",
        "data/winemag-data_first150k.csv"
    )

    print("Initial shape:", df.shape)

    # Step 3: Clean
    df = clean_data(df)
    df = add_features(df)

    print("Cleaned shape:", df.shape)

    # Step 4: Visualize
    plot_distributions(df)
    plot_country_counts(df)
    plot_relationships(df)
    plot_correlation(df)
    plot_price_category(df)

    # Step 5: Save
    save_data(df, "data/cleaned_wine_data.csv")


if __name__ == "__main__":
    main() 