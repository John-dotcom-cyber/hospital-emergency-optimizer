import streamlit as st
from modules.model import (
    compute_rho,
    classify_rho,
    optimal_staffing_for_stability,
    waiting_time_queue,
    waiting_time_system,
)
from modules.plots import rho_vs_c_plot
from modules.utils import hours_to_minutes

# ---------------------------------------------------------
# CONFIGURATION DE LA PAGE
# ---------------------------------------------------------
st.set_page_config(
    page_title="Modèle λ μ ρ — Urgences",
    page_icon="🚑",
    layout="wide"
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.title("🚑 Optimisation du Staffing aux Urgences")
st.markdown("### Interface interactive basée sur le modèle M/M/c")

st.divider()

# ---------------------------------------------------------
# SIDEBAR — PARAMÈTRES
# ---------------------------------------------------------
st.sidebar.header("⚙️ Paramètres du modèle")

lambda_val = st.sidebar.number_input("λ — Arrivées par heure", min_value=0.0, value=12.0, step=0.5)
mu_val = st.sidebar.number_input("μ — Patients traités par médecin par heure", min_value=0.1, value=3.0, step=0.1)
c_val = st.sidebar.number_input("c — Nombre de médecins", min_value=1, value=3, step=1)

rho = compute_rho(lambda_val, mu_val, c_val)
status = classify_rho(rho)

# ---------------------------------------------------------
# INDICATEUR VISUEL
# ---------------------------------------------------------
st.subheader("📊 Indicateur de tension du service")

color_map = {
    "fluide": "green",
    "sous_tension": "orange",
    "sature": "red"
}

color = color_map[status]

st.markdown(
    f"""
    <div style="padding:20px; border-radius:10px; background-color:{color}; color:white; font-size:22px; text-align:center;">
        <b>{status.replace('_', ' ').title()}</b><br>
        ρ = {rho:.2f}
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------------------------------------------------
# STAFFING OPTIMAL
# ---------------------------------------------------------
st.subheader("🧮 Staffing optimal")

optimal_c = optimal_staffing_for_stability(lambda_val, mu_val)

st.markdown(f"➡️ **Nombre minimal de médecins pour éviter la saturation : `{optimal_c}`**")

if optimal_c > c_val:
    st.warning("Le service est sous-staffé par rapport au flux actuel.")
else:
    st.success("Le staffing actuel est suffisant pour éviter la saturation.")

st.divider()

# ---------------------------------------------------------
# TEMPS D’ATTENTE
# ---------------------------------------------------------
st.subheader("⏱️ Temps d’attente estimé")

wq = waiting_time_queue(lambda_val, mu_val, c_val)
w = waiting_time_system(lambda_val, mu_val, c_val)

if w == float("inf"):
    st.error("Le système est saturé : temps d’attente théoriquement infini.")
else:
    st.write(f"Temps d’attente moyen dans la file : **{hours_to_minutes(wq):.1f} minutes**")
    st.write(f"Temps moyen dans le système : **{hours_to_minutes(w):.1f} minutes**")

st.divider()

# ---------------------------------------------------------
# GRAPHIQUE
# ---------------------------------------------------------
st.subheader("📈 Impact du nombre de médecins sur ρ")

fig = rho_vs_c_plot(lambda_val, mu_val)
st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------------------------------------------------
# ONGLET D’EXPLICATION
# ---------------------------------------------------------
tab1, tab2 = st.tabs(["📘 Comprendre λ μ ρ", "📚 Méthode scientifique"])

with tab1:
    st.markdown("## 📘 Comprendre λ, μ et ρ")
    st.markdown("""
    - **λ (lambda)** : nombre moyen de patients qui arrivent par heure  
    - **μ (mu)** : nombre de patients qu’un médecin peut traiter par heure  
    - **c** : nombre de médecins  
    - **ρ (rho)** : taux d’occupation du service  
    """)
    st.markdown("### Interprétation")
    st.markdown("""
    - ρ < 0.8 → 🟢 **Fluide**  
    - 0.8 ≤ ρ < 1 → 🟠 **Sous tension**  
    - ρ ≥ 1 → 🔴 **Saturé**  
    """)

with tab2:
    st.markdown("## 📚 Méthode scientifique — Modèle M/M/c")
    st.latex(r"\rho = \frac{\lambda}{c \mu}")
    st.latex(r"P(W>0) = \text{Erlang C}")
    st.latex(r"W_q = \frac{P(W>0)}{c\mu - \lambda}")
    st.latex(r"W = W_q + \frac{1}{\mu}")