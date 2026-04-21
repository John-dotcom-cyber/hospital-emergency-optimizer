# modules/model.py
import math

def compute_rho(lmbda: float, mu: float, c: int) -> float:
    """
    Calcule le taux d'occupation ρ = λ / (c μ).
    """
    if c <= 0 or mu <= 0:
        raise ValueError("c et μ doivent être strictement positifs.")
    return lmbda / (c * mu)


def is_stable(lmbda: float, mu: float, c: int) -> bool:
    """
    Vérifie la stabilité du système : ρ < 1.
    """
    rho = compute_rho(lmbda, mu, c)
    return rho < 1


def erlang_c(lmbda: float, mu: float, c: int) -> float:
    """
    Calcule la probabilité d'attente (Erlang C) pour un modèle M/M/c.
    """
    rho = compute_rho(lmbda, mu, c)
    if rho >= 1:
        return 1.0  # système saturé : probabilité d'attente ≈ 1

    a = lmbda / mu  # charge offerte
    sum_terms = sum((a ** k) / math.factorial(k) for k in range(c))
    last_term = (a ** c) / (math.factorial(c) * (1 - rho))
    p0 = 1.0 / (sum_terms + last_term)

    pw = last_term * p0
    return pw


def waiting_time_queue(lmbda: float, mu: float, c: int) -> float:
    """
    Temps d'attente moyen dans la file Wq (en heures).
    """
    rho = compute_rho(lmbda, mu, c)
    if rho >= 1:
        return float("inf")

    pw = erlang_c(lmbda, mu, c)
    wq = pw / (c * mu - lmbda)
    return wq


def waiting_time_system(lmbda: float, mu: float, c: int) -> float:
    """
    Temps moyen dans le système W = Wq + 1/μ (en heures).
    """
    wq = waiting_time_queue(lmbda, mu, c)
    if math.isinf(wq):
        return float("inf")
    return wq + 1.0 / mu


def optimal_staffing_for_stability(lmbda: float, mu: float) -> int:
    """
    Nombre minimal de médecins pour avoir ρ < 1.
    """
    if mu <= 0:
        raise ValueError("μ doit être strictement positif.")
    return max(1, math.floor(lmbda / mu) + 1)


def classify_rho(rho: float) -> str:
    """
    Classe ρ en trois zones : fluide / tension / saturé.
    """
    if rho < 0.8:
        return "fluide"
    elif rho < 1:
        return "sous_tension"
    else:
        return "sature"
