from analyse_charge import detect_heures_critiques, detect_jours_renfort
from planning_optimal import planning_optimal

def synthese_par_jour(df):
    critiques = df[df["zone"] == 2]
    grouped = critiques.groupby("date")["hour"].apply(list)
    lignes = []
    for date, heures in grouped.items():
        heures_str = ", ".join(f"{h:02d}h" for h in heures)
        lignes.append(f"{date} : {heures_str}")
    return "\n".join(lignes)

def score_tension(df):
    scores = df.groupby("date")["zone"].mean() * 50
    lignes = [f"{date} : {int(score)}" for date, score in scores.items()]
    return "\n".join(lignes)

def heatmap_ascii(df):
    lignes = []
    for date, group in df.groupby("date"):
        row = "".join("1" if z == 2 else "0" for z in group.sort_values("hour")["zone"])

        # Découpage en segments de 60 caractères
        segments = [row[i:i+60] for i in range(0, len(row), 60)]

        lignes.append(f"{date} :")
        for seg in segments:
            lignes.append(seg)

    return "\n".join(lignes)


def top_pics(df):
    critiques = df[df["zone"] == 2]
    if critiques.empty:
        return "Aucun pic critique détecté."

    top = critiques.nlargest(10, "lambda")
    lignes = [
        f"{row.date} {row.hour:02d}h — λ={row['lambda']}"
        for _, row in top.iterrows()
    ]
    return "\n".join(lignes)


def resume_final(df):
    nb_jours = df["date"].nunique()
    nb_critiques = (df["zone"] == 2).sum()
    pic = df["lambda"].max()
    worst_day = df.groupby("date")["zone"].sum().idxmax()
    besoin_max = df["c_opt_30min"].max()

    return (
        f"• {nb_jours} jours analysés\n"
        f"• {nb_critiques} heures critiques détectées\n"
        f"• Pic maximal : {pic} patients/h\n"
        f"• Journée la plus tendue : {worst_day}\n"
        f"• Besoin maximal : {besoin_max} médecins"
    )

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

    rapport += "\n\n===== SYNTHÈSE PAR JOUR =====\n"
    rapport += synthese_par_jour(mmc)

    rapport += "\n\n===== SCORE DE TENSION =====\n"
    rapport += score_tension(mmc)

    rapport += "\n\n===== HEATMAP ASCII =====\n"
    rapport += heatmap_ascii(mmc)

    rapport += "\n\n===== TOP 10 DES PICS =====\n"
    rapport += top_pics(mmc)

    rapport += "\n\n===== RÉSUMÉ FINAL =====\n"
    rapport += resume_final(mmc)

    return rapport


    return rapport


