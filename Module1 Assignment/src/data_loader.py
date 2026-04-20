import pandas as pd
import zipfile


def extract_zip(zip_path: str, extract_to: str) -> None:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


def load_data(file1: str, file2: str) -> pd.DataFrame:
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    df = pd.concat([df1, df2], ignore_index=True)
    return df