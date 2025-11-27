import streamlit as st
from dataset import df_master

st.title("Evidence Repository")

prev = df_master[["Nom", "Preuve_associee", "Phase", "Type_exigence"]]
st.dataframe(prev)
