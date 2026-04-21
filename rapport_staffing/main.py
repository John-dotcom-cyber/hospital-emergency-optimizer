from import_data import charger_donnees
from ajustement_charge import ajuster_charge
from rapport import generer_rapport
from preprocessing import enrichir_dataframe
from export_pdf import export_pdf


def analyser_fichier(fichier, meteo):
    mmc = charger_donnees(fichier)
    mmc = enrichir_dataframe(mmc)
    mmc = ajuster_charge(mmc, meteo)
    rapport = generer_rapport(mmc)

    fichier_pdf = export_pdf(rapport)
    print(f"PDF généré : {fichier_pdf}")

    print(rapport)


###################################### MAIN #################################################

if __name__ == "__main__":
    meteo_du_jour = {
        "temperature": 3,
        "humidite": 85,
        "pluie": 0,
        "meteo_code": "froid"
    }

    analyser_fichier("urgences_exemple.csv", meteo_du_jour)