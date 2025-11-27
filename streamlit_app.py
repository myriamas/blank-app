import streamlit as st
from dataset import (
    df_master,
    df_rflp,
    df_lifecycle,
    df_archiving,
    df_audit_trail,
)
import pandas as pd


# ----- App config -----
st.set_page_config(
    page_title="VAX-PLM – Jumeau réglementaire VIH",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----- Pages list -----
PAGES = [
    "Accueil",
    "Vue d'ensemble",
    "Exigence détaillée",
    "Tableau des exigences",
    "Documents",
    "Preuves",
    "Qualité",
    "IoT / Température",
    "Cycle de vie",
    "RFLP / Architecture",
    "Méthodologie IVV",
    "Archivage sécurisé",
    "Change control / Audit trail",
    "Soumission réglementaire",
]

# ----- Session state init -----
if "page" not in st.session_state:
    st.session_state["page"] = "Accueil"

if "selected_requirement" not in st.session_state:
    st.session_state["selected_requirement"] = None


# ----- Helpers -----
def color_statut(val: str) -> str:
    if val == "Conforme":
        return "background-color: #C8F7C5"
    if val == "Partiel":
        return "background-color: #F9E79F"
    if val == "Non conforme":
        return "background-color: #F5B7B1"
    return ""


def go_to(target: str) -> None:
    st.session_state["page"] = target
    st.rerun()



# ----- Sidebar navigation -----
st.sidebar.title("VAX-PLM – Jumeau réglementaire")
st.sidebar.write("Projet vaccin VIH – VAX-HIV-2030")

sidebar_choice = st.sidebar.radio(
    "Navigation",
    PAGES,
    index=PAGES.index(st.session_state["page"]),
)

if sidebar_choice != st.session_state["page"]:
    st.session_state["page"] = sidebar_choice

page = st.session_state["page"]


# ===========================
# ACCUEIL
# ===========================
if page == "Accueil":
    st.title("VAX-PLM – Jumeau Réglementaire du vaccin VIH")

    st.markdown(
        """
        Cette application rassemble l'ensemble du travail sur le vaccin fictif **VAX-HIV-2030** :
        exigences, documents, preuves, qualité, IoT, archivage, cycle de vie et soumission EMA/ANSM.
        """
    )

    st.markdown("### Points d'entrée principaux")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Vue globale")
        st.write("Etat de conformité des exigences et filtres par phase / type d'exigence.")
        if st.button("Ouvrir la vue d'ensemble", use_container_width=True):
            go_to("Vue d'ensemble")

        st.subheader("Lien Exigence → PLM")
        st.write("Fiche détaillée qui relie une exigence à ses documents, preuves, IoT, certificats.")
        if st.button("Ouvrir l'exigence détaillée", use_container_width=True):
            go_to("Exigence détaillée")

    with col2:
        st.subheader("Qualité")
        st.write("Stérilité, stabilité 2–8°C, validation analytique des tests VIH.")
        if st.button("Ouvrir la vue Qualité", use_container_width=True):
            go_to("Qualité")

        st.subheader("IoT / Température")
        st.write("Exemple de relevés température pour frigos et zones contrôlées.")
        if st.button("Ouvrir la vue IoT / Température", use_container_width=True):
            go_to("IoT / Température")

    with col3:
        st.subheader("Cycle de vie et RFLP")
        st.write("Vue du cycle de vie complet et synthèse Sécurité / Qualité / Efficacité / Production.")
        if st.button("Ouvrir le cycle de vie", use_container_width=True):
            go_to("Cycle de vie")
        if st.button("Ouvrir la vue RFLP / Architecture", use_container_width=True):
            go_to("RFLP / Architecture")

        st.subheader("Archivage et audit")
        st.write("Politique d'archivage 25 ans et exemple de change control / audit trail.")
        if st.button("Ouvrir l'archivage sécurisé", use_container_width=True):
            go_to("Archivage sécurisé")


# ===========================
# VUE D'ENSEMBLE
# ===========================
elif page == "Vue d'ensemble":
    st.title("Vue d'ensemble des exigences réglementaires")

    col_filters, col_table = st.columns([1, 3])

    with col_filters:
        phase = st.multiselect("Phase clinique / projet", df_master["Phase"].unique())
        type_req = st.multiselect("Type d'exigence", df_master["Type_exigence"].unique())
        statut = st.multiselect("Statut de conformité", df_master["Statut"].unique())

        df = df_master.copy()

        if phase:
            df = df[df["Phase"].isin(phase)]
        if type_req:
            df = df[df["Type_exigence"].isin(type_req)]
        if statut:
            df = df[df["Statut"].isin(statut)]

        st.markdown("**Nombre d'exigences affichées :** " + str(len(df)))

    with col_table:
        df_view = df[["Nom", "Phase", "Type_exigence", "Impact_AMM", "Statut"]].reset_index(drop=True)
        styled = df_view.style.applymap(color_statut, subset=["Statut"])
        st.dataframe(styled, use_container_width=True, hide_index=True)

    # Navigation vers fiche détaillée à partir de la vue d'ensemble
    st.markdown("### Explorer une exigence en détail")
    if len(df) > 0:
        nom_sel = st.selectbox(
            "Je sélectionne une exigence à détailler :", df_view["Nom"].tolist()
        )
        if st.button("Ouvrir la fiche détaillée depuis la vue d'ensemble"):
            st.session_state["selected_requirement"] = nom_sel
            go_to("Exigence détaillée")


# ===========================
# EXIGENCE DETAILLEE
# ===========================
elif page == "Exigence détaillée":
    st.title("Exigence détaillée – Exigence → Documents → Preuves")

    options = df_master["Nom"].tolist()
    if st.session_state["selected_requirement"] in options:
        default_index = options.index(st.session_state["selected_requirement"])
    else:
        default_index = 0

    choix = st.selectbox(
        "Je sélectionne une exigence :", options, index=default_index
    )
    st.session_state["selected_requirement"] = choix

    ligne = df_master[df_master["Nom"] == choix].iloc[0]

    col_meta, col_docs = st.columns(2)

    with col_meta:
        st.subheader("Résumé de l'exigence")
        st.write(f"**Nom :** {ligne['Nom']}")
        st.write(f"**Phase :** {ligne['Phase']}")
        st.write(f"**Type d'exigence :** {ligne['Type_exigence']}")
        st.write(f"**Impact sur l'AMM :** {ligne['Impact_AMM']}")
        st.write(f"**Statut :** {ligne['Statut']}")
        st.write("**Description :**")
        st.write(ligne["Description"])

    with col_docs:
        st.subheader("Liens PLM associés")
        st.write(f"**Document(s) lié(s) :** {ligne['Documents_lies']}")
        st.write(f"**Preuve(s) liée(s) :** {ligne['Preuves_liees']}")
        if ligne["IoT"]:
            st.write(f"**IoT / mesure associée :** {ligne['IoT']} ({ligne['Frequence']})")
        if ligne["Certificat_etalonnage"]:
            st.write(f"**Certificat d'étalonnage :** {ligne['Certificat_etalonnage']}")
        st.write(f"**Processus qualité :** {ligne['Process_qualite']}")
        st.write(f"**Référence de fiche / protocole :** {ligne['Fiche_protocole']}")


# ===========================
# TABLEAU DES EXIGENCES
# ===========================
elif page == "Tableau des exigences":
    st.title("Tableau complet des exigences")

    df_view = df_master[
        [
            "Nom",
            "Type_element",
            "Phase",
            "Type_exigence",
            "Description",
            "Impact_AMM",
            "Statut",
        ]
    ].reset_index(drop=True)

    st.dataframe(df_view, use_container_width=True, hide_index=True)

    # lien vers fiche détaillée
    nom_sel = st.selectbox(
        "Voir la fiche détaillée d'une exigence :", df_view["Nom"].tolist()
    )
    if st.button("Ouvrir la fiche détaillée depuis le tableau des exigences"):
        st.session_state["selected_requirement"] = nom_sel
        go_to("Exigence détaillée")


# ===========================
# DOCUMENTS
# ===========================
elif page == "Documents":
    st.title("Documents liés aux exigences")

    docs = df_master[
        ["Nom", "Documents_lies", "Fiche_protocole", "Phase", "Type_exigence", "Statut"]
    ].reset_index(drop=True)

    st.dataframe(docs, use_container_width=True, hide_index=True)

    nom_sel = st.selectbox(
        "Voir la fiche détaillée à partir d'un document :", docs["Nom"].tolist()
    )
    if st.button("Ouvrir la fiche détaillée depuis Documents"):
        st.session_state["selected_requirement"] = nom_sel
        go_to("Exigence détaillée")


# ===========================
# PREUVES
# ===========================
elif page == "Preuves":
    st.title("Preuves associées aux exigences")

    evid = df_master[
        ["Nom", "Preuves_liees", "Impact_AMM", "Type_exigence", "Phase", "Statut"]
    ].reset_index(drop=True)

    st.dataframe(evid, use_container_width=True, hide_index=True)

    nom_sel = st.selectbox(
        "Voir la fiche détaillée à partir d'une preuve :", evid["Nom"].tolist()
    )
    if st.button("Ouvrir la fiche détaillée depuis Preuves"):
        st.session_state["selected_requirement"] = nom_sel
        go_to("Exigence détaillée")


# ===========================
# QUALITE
# ===========================
elif page == "Qualité":
    st.title("Vue Qualité (stérilité, stabilité, méthodes analytiques)")

    quality = df_master[df_master["Type_exigence"] == "Qualité"].copy()

    # tableau synthétique sans scroll horizontal
    df_summary = quality[
        ["Nom", "Phase", "Statut", "Process_qualite"]
    ].reset_index(drop=True)
    st.subheader("Synthèse Qualité")
    st.dataframe(df_summary, use_container_width=True, hide_index=True)

    # tous les détails dans un expander
    with st.expander("Afficher le détail complet Qualité (toutes les colonnes)"):
        df_full = quality[
            [
                "Nom",
                "Description",
                "Phase",
                "Statut",
                "Impact_AMM",
                "Process_qualite",
                "Certificat_etalonnage",
            ]
        ].reset_index(drop=True)
        st.dataframe(df_full, use_container_width=True, hide_index=True)

    nom_sel = st.selectbox(
        "Voir la fiche détaillée d'une exigence qualité :", df_summary["Nom"].tolist()
    )
    if st.button("Ouvrir la fiche détaillée depuis Qualité"):
        st.session_state["selected_requirement"] = nom_sel
        go_to("Exigence détaillée")


# ===========================
# IOT / TEMPERATURE
# ===========================
elif page == "IoT / Température":
    st.title("IoT / Température – chaîne du froid et salles contrôlées")

    data_iot = {
        "Capteur": ["Frigo clinique 01", "Frigo QC 02", "Salle de stockage"],
        "Localisation": ["Site clinique A", "Laboratoire QC", "Entrepôt GMP"],
        "Température": ["7.2°C", "6.8°C", "20.5°C"],
        "Fréquence mesure": ["Toutes les 10 min", "Toutes les 10 min", "Toutes les 60 min"],
        "Statut alerte": ["OK", "OK", "Hors spécification"],
    }

    df_iot = pd.DataFrame(data_iot).reset_index(drop=True)
    st.dataframe(df_iot, use_container_width=True, hide_index=True)


# ===========================
# CYCLE DE VIE
# ===========================
elif page == "Cycle de vie":
    st.title("Cycle de vie du vaccin – VAX-HIV-2030")

    st.dataframe(df_lifecycle.reset_index(drop=True), use_container_width=True, hide_index=True)


# ===========================
# RFLP / ARCHITECTURE
# ===========================
elif page == "RFLP / Architecture":
    st.title("Vue RFLP – Sécurité / Qualité / Efficacité / Production")

    st.subheader("Synthèse RFLP")
    st.dataframe(df_rflp.reset_index(drop=True), use_container_width=True, hide_index=True)

    st.subheader("Architecture logique (vue simplifiée)")
    st.markdown(
        """
        1. Antigène / plateforme vaccinale  
        2. Formulation (vecteur, adjuvant)  
        3. Administration intramusculaire et logistique  
        4. Réponse immunitaire (humorale + cellulaire)  
        5. Contrôles qualité et libération des lots
        """
    )


# ===========================
# METHODOLOGIE IVV
# ===========================
elif page == "Méthodologie IVV":
    st.title("Méthodologie IVV – Intégration, Vérification, Validation")

    st.markdown(
        """
        - **Intégration** : relier exigences, change control, jumeau réglementaire et archivage  
          avec des identifiants communs et des rôles clairs.  
        - **Vérification** : vérifier les règles GxP (Annexe 11, 21 CFR Part 11, intégrité des données) :  
          audit trail, droits d'accès, cohérence des statuts.  
        - **Validation** : rejouer des scénarios complets (Exigence → Changement → Document mis à jour  
          → Preuve archivée) et montrer le résultat dans ce jumeau numérique.
        """
    )


# ===========================
# ARCHIVAGE SECURISE
# ===========================
elif page == "Archivage sécurisé":
    st.title("Politique d'archivage sécurisé – VIH")

    st.dataframe(df_archiving.reset_index(drop=True), use_container_width=True, hide_index=True)

    st.markdown(
        """
        Je garde aussi :
        - Versioning et audit trail pour tous les documents GxP  
        - Métadonnées complètes (ID, version, date, statut, hash)  
        - Capacité à retrouver une preuve en quelques secondes lors d'une inspection
        """
    )


# ===========================
# CHANGE CONTROL / AUDIT TRAIL
# ===========================
elif page == "Change control / Audit trail":
    st.title("Change control et audit trail – exemple de scénario")

    st.write("Exemple de changement réglementaire sur le vaccin VIH et impact sur le PLM.")
    st.dataframe(
        df_audit_trail.reset_index(drop=True),
        use_container_width=True,
        hide_index=True,
    )


# ===========================
# SOUMISSION REGLEMENTAIRE
# ===========================
elif page == "Soumission réglementaire":
    st.title("Soumission réglementaire – EMA / ANSM")

    st.markdown(
        """
        - Procédure centralisée EMA (Règlement (CE) 726/2004)  
        - Code communautaire des médicaments (Directive 2001/83/CE)  
        - Dossier CTD complet : qualité, sécurité, efficacité  
        - Étapes nationales France (ANSM, HAS) et mise en place de la pharmacovigilance  
        - Le jumeau réglementaire sert à montrer **où** se trouvent les documents et preuves
          associés à chaque exigence, en quelques clics.
        """
    )
