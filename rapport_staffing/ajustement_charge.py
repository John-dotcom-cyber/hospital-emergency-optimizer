from analyse_saisonnalite import facteur_saisonnalite
from analyse_meteo import facteur_meteo

def ajuster_charge(mmc, meteo):
    """
    Ajoute une colonne 'charge_ajustee' basée sur :
    - saisonnalité
    - météo
    """

    mmc["facteur_saison"] = mmc["date"].apply(facteur_saisonnalite)
    mmc["facteur_meteo"] = facteur_meteo(meteo)

    mmc["charge_ajustee"] = (
        mmc["lambda"] *
        mmc["facteur_saison"] *
        mmc["facteur_meteo"]
    )

    return mmc
