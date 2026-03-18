import pandas as pd
from pathlib import Path

def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file and return a DataFrame."""
    return pd.read_csv(path)

def save_parquet(df: pd.DataFrame, path: str) -> None:
    """Save a DataFrame to Parquet."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
