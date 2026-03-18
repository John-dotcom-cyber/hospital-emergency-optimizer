# 🏗️ Architecture Fonctionnelle — Hospital Emergency Optimizer

## 1. Vue d’ensemble

La plateforme est organisée en quatre modules principaux, conçus pour fonctionner ensemble mais utilisables indépendamment :

1. **Prédiction du flux d’arrivées**
2. **Simulation des files d’attente**
3. **Optimisation des ressources**
4. **Tableau de bord temps réel**

Chaque module repose sur une couche commune :
- ingestion et harmonisation des données,
- stockage structuré,
- API interne,
- moteur de calcul.

---

## 2. Modules fonctionnels

### 🔮 1. Module de prédiction
Fonctionnalités :
- Prévision du nombre d’arrivées par heure / jour
- Modèles de séries temporelles (Prophet, SARIMA, LSTM…)
- Intégration de variables externes :
  - météo
  - épidémies
  - saisonnalité
  - événements locaux
- Détection des anomalies

Entrées :
- historique des urgences
- données externes

Sorties :
- prédictions
- intervalles de confiance
- alertes

---

### 🧪 2. Module de simulation
Fonctionnalités :
- Simulation des files d’attente (modèles de files M/M/1, M/M/c…)
- Simulation multi-étapes (triage → box → examens → sortie)
- Scénarios paramétrables :
  - variation du personnel
  - variation du flux
  - saturation des lits
  - modification du triage
- Visualisation des résultats

Entrées :
- prédictions
- paramètres de scénario

Sorties :
- temps d’attente simulés
- taux d’occupation
- goulots d’étranglement

---

### 🧠 3. Module d’optimisation
Fonctionnalités :
- Allocation optimale du personnel
- Optimisation des lits et salles
- Recommandations d’organisation
- Contraintes configurables :
  - effectifs minimum
  - compétences
  - horaires
  - matériel disponible

Entrées :
- prédictions
- résultats de simulation
- contraintes opérationnelles

Sorties :
- planning optimal
- recommandations actionnables

---

### 📊 4. Tableau de bord temps réel
Fonctionnalités :
- Vue en temps réel de l’activité
- Alertes prédictives
- Visualisation des files d’attente
- Recommandations automatiques
- Intégration possible avec Power BI

Entrées :
- données en temps réel
- prédictions
- optimisation

Sorties :
- interface utilisateur
- alertes
- KPIs

---

## 3. Couche commune

### 📥 Ingestion & harmonisation
- Import CSV / API / base SQL
- Détection automatique des colonnes
- Harmonisation intelligente
- Nettoyage et validation

### 🗄️ Stockage
- fichiers parquet / SQL
- versioning des données
- logs d’ingestion

### ⚙️ Moteur de calcul
- orchestrateur interne
- exécution des modèles
- gestion des dépendances

### 🔌 API interne
- endpoints pour le dashboard
- endpoints pour les modules
