import pandas as pd
import numpy as np

# Génération d'un dataset synthétique sur 90 jours, pas horaire
date_range = pd.date_range(start="2024-01-01", end="2024-03-31", freq="H")

df = pd.DataFrame({"datetime": date_range})

# Base : 5 à 20 arrivées par heure
base = 10

# Effet heure de la journée (pics 17h-22h)
df["hour"] = df["datetime"].dt.hour
df["hour_effect"] = df["hour"].apply(lambda h: 
    5 if 17 <= h <= 22 else 
    3 if 10 <= h <= 16 else 
    1
)

# Effet jour de la semaine (lundi plus chargé)
df["dow"] = df["datetime"].dt.dayofweek
df["dow_effect"] = df["dow"].apply(lambda d: 
    4 if d == 0 else 
    2 if d in [1,2,3] else 
    3
)

# Bruit aléatoire
np.random.seed(42)
df["noise"] = np.random.normal(0, 2, len(df))

# Calcul final
df["arrivals"] = (base 
                  + df["hour_effect"] 
                  + df["dow_effect"] 
                  + df["noise"]).round().clip(lower=0)

# Nettoyage
df = df[["datetime", "arrivals"]]

# Sauvegarde
df.to_csv("data/examples/urgences_exemple.csv", index=False)

df.head()
