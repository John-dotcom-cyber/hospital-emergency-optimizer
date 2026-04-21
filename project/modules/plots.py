# modules/plots.py
import numpy as np
import pandas as pd
import plotly.express as px
from .model import compute_rho

def rho_vs_c_dataframe(lmbda: float, mu: float, c_max: int = 15) -> pd.DataFrame:
    """
    Construit un DataFrame avec ρ en fonction du nombre de médecins c.
    """
    c_range = np.arange(1, c_max + 1)
    rho_values = [compute_rho(lmbda, mu, c) for c in c_range]
    return pd.DataFrame({"Médecins": c_range, "ρ": rho_values})


def rho_vs_c_plot(lmbda: float, mu: float, c_max: int = 15):
    """
    Crée un graphique Plotly de ρ en fonction de c.
    """
    df = rho_vs_c_dataframe(lmbda, mu, c_max)
    fig = px.line(
        df,
        x="Médecins",
        y="ρ",
        markers=True,
        title="Évolution du taux d’occupation en fonction du nombre de médecins",
    )
    fig.add_hline(y=1, line_dash="dash", line_color="red")
    fig.add_hline(y=0.8, line_dash="dash", line_color="orange")
    return fig
