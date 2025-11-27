import streamlit as st
from dataset import df_master

st.title("Regulatory Dashboard")

st.write("Vue synthétique de la conformité réglementaire du vaccin VIH.")

# Status color coding
def color_statut(val):
    if val == "Conforme":
        return "background-color: #C8F7C5"
    elif val == "Partiel":
        return "background-color: #F9E79F"
    else:
        return "background-color: #F5B7B1"

st.dataframe(df_master.style.applymap(color_statut, subset=["Statut"]))
