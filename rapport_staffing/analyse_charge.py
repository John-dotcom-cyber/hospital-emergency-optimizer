def detect_heures_critiques(mmc):
    """
    Identifie les heures critiques selon :
    - zone rouge (rho > 0.85)
    - besoin élevé (>= 7 médecins)
    - écart 15min vs 30min >= 1 médecin
    """

    heures_critiques = mmc[
        (mmc["zone"] == 2) |
        (mmc["c_opt_30min"] >= 7) |
        ((mmc["c_opt_15min"] - mmc["c_opt_30min"]) >= 1)
    ].copy()

    def commentaire(row):
        if row["zone"] == 2:
            return "Pointe (rho > 0.85)"
        if row["c_opt_30min"] >= 7:
            return "Besoin élevé (≥7 médecins)"
        if (row["c_opt_15min"] - row["c_opt_30min"]) >= 1:
            return "15 min plus exigeant"
        return "Normal"

    heures_critiques["commentaire"] = heures_critiques.apply(commentaire, axis=1)
    return heures_critiques


def detect_jours_renfort(mmc):
    """
    Classe les jours selon leur niveau de tension moyen.
    """
    jours = mmc.groupby("weekday")["zone"].mean().sort_values(ascending=False)

    jours_rouges = jours[jours >= 1.5].index.tolist()
    jours_orange = jours[(jours >= 0.8) & (jours < 1.5)].index.tolist()
    jours_verts = jours[jours < 0.8].index.tolist()

    return jours_rouges, jours_orange, jours_verts
