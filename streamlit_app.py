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

# ----- Session state for navigation (so buttons can change pages) -----
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

if "page" not in st.session_state:
    st.session_state["page"] = "Accueil"


# ----- Helper for status coloring -----
def color_statut(val: str) -> str:
    if val == "Conforme":
        return "background-color: #C8F7C5"
    if val == "Partiel":
        return "background-color: #F9E79F"
    if val == "Non conforme":
        return "background-color: #F5B7B1"
    return ""


# ----- Sidebar navigation -----
st.sidebar.title("VAX-PLM – Jumeau réglementaire")
st.sidebar.write("Projet vaccin VIH – VAX-HIV-2030")

sidebar_choice = st.sidebar.radio(
    "Navigation",
    PAGES,
    index=PAGES.index(st.session_state["page"]),
)

# Sync sidebar choice with session state
if sidebar_choice != st.session_state["page"]:
    st.session_state["page"] = sidebar_choice

page = st.session_state["page"]


# ----- Small helper to go to a page from buttons -----
def go_to(target: str) -> None:
    st.session_state["page"] = target
    st.rerun()


# ----- ACCUEIL -----
if page == "Accueil":
    st.title("VAX-PLM – Jumeau Réglementaire du vaccin VIH")

    st.markdown(
        """
        Cette application présente le **jumeau réglementaire** du vaccin fictif VAX-HIV-2030.
        Je regroupe ici toutes les briques du projet : exigences, documents, preuves, qualité,
        IoT, archivage, cycle de vie et soumission EMA/ANSM.
        """
    )

    st.markdown("### Par où je commence ?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("####  Vue globale")
        st.write("Etat de conformité des exigences (vert / orange / rouge).")
        if st.button("Aller à la vue d'ensemble", use_container_width=True):
            go_to("Vue d'ensemble")

        st.markdown("####  Exigence → Doc → Preuves")
        st.write("Je choisis une exigence et je vois tous les liens PLM associés.")
        if st.button("Aller à l'exigence détaillée", use_container_width=True):
            go_to("Exigence détaillée")

    with col2:
        st.markdown("####  Qualité & chaîne du froid")
        st.write("Stérilité, stabilité 2–8°C, validation analytique.")
        if st.button("Voir la vue Qualité", use_container_width=True):
            go_to("Qualité")

        st.markdown("####  IoT / Température")
        st.write("Exemple de relevés température pour frigos et salles.")
        if st.button("Voir la vue IoT / Température", use_container_width=True):
            go_to("IoT / Température")

    with col3:
        st.markdown("####  Cycle de vie & RFLP")
        st.write("Du concept jusqu'à la pharmacovigilance + vue RFLP du projet.")
        if st.button("Voir le cycle de vie", use_container_width=True):
            go_to("Cycle de vie")
        if st.button("Voir la vue RFLP / Architecture", use_container_width=True):
            go_to("RFLP / Architecture")

        st.markdown("####  Archivage & audit")
        st.write("Politique d'archivage 25 ans et exemple d'audit trail.")
        if st.button("Archivage sécurisé", use_container_width=True):
            go_to("Archivage sécurisé")


# ----- VUE D'ENSEMBLE -----
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
        df_view = df[
            ["Nom", "Phase", "Type_exigence", "Impact_AMM", "Statut"]
        ].reset_index(drop=True)
        styled = df_view.style.applymap(color_statut, subset=["Statut"]).hide(axis="index")
        st.dataframe(styled, use_container_width=True)


# ----- EXIGENCE DETAILLEE -----
elif page == "Exigence détaillée":
    st.title("Exigence détaillée – Exigence → Documents → Preuves")

    choix = st.selectbox("Je sélectionne une exigence :", df_master["Nom"].tolist())

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


# ----- TABLEAU DES EXIGENCES -----
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

    st.dataframe(df_view, use_container_width=True)


# ----- DOCUMENTS -----
elif page == "Documents":
    st.title("Documents liés aux exigences")

    docs = df_master[
        ["Nom", "Documents_lies", "Fiche_protocole", "Phase", "Type_exigence", "Statut"]
    ].reset_index(drop=True)

    st.dataframe(docs, use_container_width=True)


# ----- PREUVES -----
elif page == "Preuves":
    st.title("Preuves associées aux exigences")

    evid = df_master[
        ["Nom", "Preuves_liees", "Impact_AMM", "Type_exigence", "Phase", "Statut"]
    ].reset_index(drop=True)

    st.dataframe(evid, use_container_width=True)


# ----- QUALITE -----
elif page == "Qualité":
    st.title("Vue Qualité (stérilité, stabilité, méthodes analytiques)")

    quality = df_master[df_master["Type_exigence"] == "Qualité"].copy()
    df_view = quality[
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

    st.dataframe(df_view, use_container_width=True)


# ----- IOT / TEMPERATURE -----
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
    st.dataframe(df_iot, use_container_width=True)


# ----- CYCLE DE VIE -----
elif page == "Cycle de vie":
    st.title("Cycle de vie du vaccin – VAX-HIV-2030")

    st.dataframe(df_lifecycle.reset_index(drop=True), use_container_width=True)


# ----- RFLP / ARCHITECTURE -----
elif page == "RFLP / Architecture":
    st.title("Vue RFLP – Sécurité / Qualité / Efficacité / Production")

    st.subheader("Synthèse RFLP")
    st.dataframe(df_rflp.reset_index(drop=True), use_container_width=True)

    st.subheader("Architecture logique (vue simplifiée)")
    st.markdown(
        """
        1. Antigène / plateforme vaccinale  
        2. Formulation (vecteur, adjuvant)  
        3. Administration (IM) et logistique  
        4. Réponse immunitaire (humorale + cellulaire)  
        5. Contrôles qualité et libération des lots
        """
    )


# ----- METHODOLOGIE IVV -----
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


# ----- ARCHIVAGE SECURISE -----
elif page == "Archivage sécurisé":
    st.title("Politique d'archivage sécurisé – VIH")

    st.dataframe(df_archiving.reset_index(drop=True), use_container_width=True)

    st.markdown(
        """
        Je garde aussi :
        - Versioning et audit trail pour tous les documents GxP  
        - Métadonnées complètes (ID, version, date, statut, hash)  
        - Capacité à retrouver une preuve en quelques secondes lors d'une inspection
        """
    )


# ----- CHANGE CONTROL / AUDIT TRAIL -----
elif page == "Change control / Audit trail":
    st.title("Change control et audit trail – exemple de scénario")

    st.write("Exemple de changement réglementaire sur le vaccin VIH et son impact PLM.")
    st.dataframe(df_audit_trail.reset_index(drop=True), use_container_width=True)


# ----- SOUMISSION REGLEMENTAIRE -----
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
