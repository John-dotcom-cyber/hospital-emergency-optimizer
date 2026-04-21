# modules/utils.py

def hours_to_minutes(hours: float) -> float:
    """
    Convertit un temps en heures vers des minutes.
    """
    return hours * 60.0


def safe_float(value, default=None):
    """
    Convertit en float en gérant les erreurs.
    """
    try:
        return float(value)
    except (TypeError, ValueError):
        return default