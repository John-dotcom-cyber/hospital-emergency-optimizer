# 🧬 Architecture Technique — Hospital Emergency Optimizer

## 1. Vue globale

L’architecture technique repose sur quatre couches :

1. **Ingestion & harmonisation**
2. **Pipeline de traitement**
3. **Moteurs de calcul (prédiction, simulation, optimisation)**
4. **Exposition (API + dashboard)**

---

## 2. Ingestion & harmonisation

### Sources possibles :
- exports SIH (urgences, UHCD…)
- données météo
- données épidémiologiques
- données internes (planning, lits)

### Pipeline :
- détection automatique du schéma
- mapping intelligent des colonnes
- validation des types
- nettoyage
- enrichissement
- stockage en parquet

---

## 3. Pipeline de traitement

### Étapes :
- feature engineering
- agrégation temporelle
- normalisation
- préparation pour les modèles
- stockage intermédiaire

Technos possibles :
- pandas / polars
- dask pour le scaling
- pyarrow pour le stockage

---

## 4. Moteur de prédiction

Modèles possibles :
- Prophet
- SARIMA
- XGBoost
- LSTM / GRU

Fonctionnalités :
- entraînement automatique
- sélection de modèle
- backtesting
- génération d’alertes

---

## 5. Moteur de simulation

Modèles :
- files d’attente M/M/1, M/M/c
- simulation multi-étapes
- simulation événementielle discrète

Technos :
- simpy
- numpy

---

## 6. Moteur d’optimisation

Méthodes :
- programmation linéaire
- heuristiques
- recherche locale
- contraintes personnalisées

Technos :
- pulp
- ortools

---

## 7. Exposition & interface

### API interne :
- FastAPI
- endpoints pour :
  - prédictions
  - simulation
  - optimisation
  - données temps réel

### Dashboard :
- Streamlit (MVP)
- Power BI (production)

---

## 8. Sécurité & conformité

- anonymisation des données
- logs d’accès
- séparation des environnements
- conformité RGPD
