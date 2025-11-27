import streamlit as st
from dataset import df_master

st.title("Quality Control")

quality = df_master[df_master["Type_exigence"] == "Qualité"]
st.dataframe(quality)
