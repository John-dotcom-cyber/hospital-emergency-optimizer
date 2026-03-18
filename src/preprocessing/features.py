import pandas as pd

def add_time_features(df: pd.DataFrame, datetime_col: str) -> pd.DataFrame:
    df = df.copy()
    dt = pd.to_datetime(df[datetime_col])
    df["hour"] = dt.dt.hour
    df["dayofweek"] = dt.dt.dayofweek
    df["month"] = dt.dt.month
    return df
