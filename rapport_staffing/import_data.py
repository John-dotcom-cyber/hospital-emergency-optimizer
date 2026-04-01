import pandas as pd

def charger_donnees(fichier):
    """
    Charge un fichier CSV ou Excel et renvoie un DataFrame.
    """
    if fichier.endswith(".csv"):
        return pd.read_csv(fichier)
    elif fichier.endswith(".xlsx") or fichier.endswith(".xls"):
        return pd.read_excel(fichier)
    else:
        raise ValueError("Format non supporté. Utilise CSV ou Excel.")
