def facteur_meteo(meteo):
    """
    meteo = dict :
    - temperature
    - humidite
    - pluie
    - meteo_code
    """

    facteur = 1.0

    if meteo["temperature"] < 5:
        facteur += 0.15

    if meteo["temperature"] > 32:
        facteur += 0.10

    if meteo["humidite"] > 80:
        facteur += 0.10

    if meteo["pluie"] > 5:
        facteur -= 0.05

    if meteo["meteo_code"] == "neige":
        facteur += 0.20

    return facteur
