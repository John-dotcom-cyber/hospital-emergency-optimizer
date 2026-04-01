def facteur_saisonnalite(date):
    mois = date.month

    if mois in [12, 1, 2]:
        return 1.25   # hiver : +25%
    if mois in [10, 11]:
        return 1.15   # automne : +15%
    if mois in [3, 4]:
        return 1.10   # printemps : +10%
    if mois in [5, 6, 7, 8]:
        return 0.95   # été : -5%
    return 1.0
