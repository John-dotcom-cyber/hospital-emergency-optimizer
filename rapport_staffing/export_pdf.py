from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def export_pdf(texte, nom_fichier="rapport_staffing.pdf"):
    c = canvas.Canvas(nom_fichier, pagesize=A4)
    width, height = A4

    # Position de départ
    x = 20 * mm
    y = height - 20 * mm

    # Police standard (UTF-8 safe)
    c.setFont("Helvetica", 10)

    for ligne in texte.split("\n"):
        # Si on arrive en bas de page → nouvelle page
        if y < 20 * mm:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = height - 20 * mm

        # On dessine la ligne
        c.drawString(x, y, ligne)
        y -= 5 * mm

    c.save()
    return nom_fichier
