import streamlit as st
import pandas as pd

st.set_page_config(page_title="VAX-PLM", layout="wide")

st.title("VAX-HIV-2030 – Digital Regulatory Twin")
st.write("Dashboard réglementaire : Exigences ↔ Documents ↔ Preuves")

st.sidebar.header("Importer les données réglementaires")

exigences_file = st.sidebar.file_uploader("Exigences réglementaires (CSV)")
documents_file = st.sidebar.file_uploader("Documents réglementaires (CSV)")
preuves_file = st.sidebar.file_uploader("Preuves réglementaires (CSV)")

if exigences_file:
    exigences = pd.read_csv(exigences_file)
    st.subheader("Exigences réglementaires")
    st.dataframe(exigences)

if documents_file:
    documents = pd.read_csv(documents_file)
    st.subheader("Documents réglementaires")
    st.dataframe(documents)

if preuves_file:
    preuves = pd.read_csv(preuves_file)
    st.subheader("Preuves réglementaires")
    st.dataframe(preuves)

if exigences_file and documents_file and preuves_file:
    st.subheader("Fusion PLM – Vue complète")

    fusion = exigences.copy()

    # I standardize data types for merge
    fusion["Documents associés"] = fusion["Documents associés"].astype(str)
    fusion["Preuves associées"] = fusion["Preuves associées"].astype(str)
    documents["Nom"] = documents["Nom"].astype(str)
    preuves["Name"] = preuves["Name"].astype(str)

    fusion["Documents associés"].replace("nan", "", inplace=True)
    fusion["Preuves associées"].replace("nan", "", inplace=True)

    # Merge documents
    if "Documents associés" in fusion.columns and "Nom" in documents.columns:
        fusion = fusion.merge(
            documents,
            left_on="Documents associés",
            right_on="Nom",
            how="left",
            suffixes=("", "_doc")
        )

    # Merge proofs
    if "Preuves associées" in fusion.columns and "Name" in preuves.columns:
        fusion = fusion.merge(
            preuves,
            left_on="Preuves associées",
            right_on="Name",
            how="left",
            suffixes=("", "_preuve")
        )

    st.dataframe(fusion)
