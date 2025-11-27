import streamlit as st
import pandas as pd
import altair as alt

st.title("Qualité, IoT, Stabilité et Calibration – VAX-HIV-2030")

file = st.sidebar.file_uploader("Importer Exigences (CSV) pour extraire les données qualité", key="qual_req")

if file:
    df = pd.read_csv(file)

    quality_df = df[df["Type d’exigence"].isin(["Qualité", "Production", "Pharmacovigilance"])]

    st.subheader("Exigences qualité filtrées")
    st.dataframe(quality_df)

    if "IoT" in df.columns and df["IoT"].notna().sum() > 0:
        iot_df = df[df["IoT"].notna()][["Nom", "IoT"]]

        st.subheader("Relevés IoT déclarés")
        st.dataframe(iot_df)

    if "Fréquence de mesure" in df.columns:
        freq_df = df[df["Fréquence de mesure"].notna()][["Nom", "Fréquence de mesure"]]
        st.subheader("Fréquence de mesure")
        st.dataframe(freq_df)

    if "Statut conformité" in quality_df.columns:
        st.subheader("Distribution conformité qualité")

        bar = alt.Chart(quality_df).mark_bar().encode(
            x='Statut conformité',
            y='count()',
            color='Statut conformité'
        )

        st.altair_chart(bar, use_container_width=True)
