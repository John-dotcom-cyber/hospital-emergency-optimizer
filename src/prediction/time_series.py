import pandas as pd
from neuralprophet import NeuralProphet

def train_prophet(df: pd.DataFrame, date_col: str, target_col: str):
    model_df = df[[date_col, target_col]].rename(columns={date_col: "ds", target_col: "y"})
    model = NeuralProphet()
    model.fit(model_df, freq="H")
    return model

def forecast_prophet(model, df, periods: int, freq: str = "H"):
    future = model.make_future_dataframe(
        df=df,
        periods=periods,
        n_historic_predictions=True
    )
    forecast = model.predict(future)
    return forecast


