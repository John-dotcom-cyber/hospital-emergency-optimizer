import pandas as pd
from neuralprophet import NeuralProphet

def train_prophet(df: pd.DataFrame, date_col: str, target_col: str):
    model_df = df[[date_col, target_col]].rename(columns={date_col: "ds", target_col: "y"})
    model = NeuralProphet()
    model.fit(model_df, freq="H")
    return model

def forecast_prophet(model, periods: int, freq: str = "H"):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

