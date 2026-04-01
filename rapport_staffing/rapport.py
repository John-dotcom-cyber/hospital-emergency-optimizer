from analyse_charge import detect_heures_critiques, detect_jours_renfort
from planning_optimal import planning_optimal

def generer_rapport(mmc):

    heures_critiques = detect_heures_critiques(mmc)
    jours_rouges, jours_orange, jours_verts = detect_jours_renfort(mmc)
    planning = planning_optimal()

    rapport = "\n================ RAPPORT SYNTHÉTIQUE =================\n\n"

    rapport += "1. RÉSUMÉ EXÉCUTIF\n"
    rapport += "Analyse des pics de charge et recommandations de staffing.\n\n"

    rapport += "2. JOURS À RENFORCER\n"
    rapport += f"- Renfort structurel : {', '.join(jours_rouges)}\n"
    rapport += f"- Renfort partiel : {', '.join(jours_orange)}\n"
    rapport += f"- Pas de renfort : {', '.join(jours_verts)}\n\n"

    rapport += "3. PLANNING OPTIMAL\n"
    for plage, besoin in planning.items():
        rapport += f"- {plage} : {besoin}\n"
    rapport += "\n"

    rapport += "4. HEURES CRITIQUES\n"
    rapport += heures_critiques[["date", "hour", "commentaire"]].to_string(index=False)
    rapport += "\n\n=======================================================\n"

    return rapport
