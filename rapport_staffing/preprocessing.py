import pandas as pd
import numpy as np

# Paramètre du modèle M/M/c
MU = 4.0  # capacité moyenne d'un médecin (patients/heure)

def calculer_rho(lambda_, c):
    return lambda_ / (c * MU)

def erlang_c(lambda_, c):
    rho = calculer_rho(lambda_, c)
    if rho >= 1:
        return 1.0

    sum_terms = sum((lambda_ / MU)**k / np.math.factorial(k) for k in range(c))
    last_term = ((lambda_ / MU)**c / np.math.factorial(c)) * (1 / (1 - rho))
    p0 = 1 / (sum_terms + last_term)
    pc = last_term * p0
    return pc

def temps_attente(lambda_, c):
    # éviter la division par zéro
    if c * MU <= lambda_:
        return float('inf')

    pc = erlang_c(lambda_, c)
    return pc / (c * MU - lambda_)


def trouver_c_optimal(lambda_, objectif_minutes):
    objectif_heures = objectif_minutes / 60

    # minimum théorique
    c_min = max(1, int(np.ceil(lambda_ / MU)))

    for c in range(c_min, c_min + 20):
        wq = temps_attente(lambda_, c)
        if wq <= objectif_heures:
            return c

    return c_min + 20



def enrichir_dataframe(df):
    df["datetime"] = pd.to_datetime(df["datetime"])
    df["date"] = df["datetime"].dt.date
    df["hour"] = df["datetime"].dt.hour
    df["weekday"] = df["datetime"].dt.day_name()

    df["lambda"] = df["arrivals"]

    df["c_opt_30min"] = df["lambda"].apply(lambda x: trouver_c_optimal(x, 30))
    df["c_opt_15min"] = df["lambda"].apply(lambda x: trouver_c_optimal(x, 15))

    df["rho"] = df.apply(lambda row: calculer_rho(row["lambda"], row["c_opt_30min"]), axis=1)

    df["zone"] = df["rho"].apply(lambda r: 2 if r > 0.85 else (1 if r > 0.6 else 0))

    return df
