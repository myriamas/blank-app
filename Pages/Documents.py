import streamlit as st
from dataset import df_master

st.title("Documents Repository")

docs = df_master[["Nom", "Document_associe", "Phase", "Statut"]]
st.dataframe(docs)
