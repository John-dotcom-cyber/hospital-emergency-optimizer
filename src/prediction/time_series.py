import pandas as pd
from prophet import Prophet

def train_prophet(df: pd.DataFrame, date_col: str, target_col: str) -> Prophet:
    model_df = df[[date_col, target_col]].rename(columns={date_col: "ds", target_col: "y"})
    model = Prophet()
    model.fit(model_df)
    return model

def forecast_prophet(model: Prophet, periods: int, freq: str = "H") -> pd.DataFrame:
    future = model.make_future_dataframe(periods=periods, freq=freq)
    forecast = model.predict(future)
    return forecast
