import streamlit as st
from dataset import df_master

st.title("Requirements Repository")

phase = st.sidebar.multiselect("Filter by Phase", df_master["Phase"].unique())
type_req = st.sidebar.multiselect("Filter by Requirement Type", df_master["Type_exigence"].unique())

df = df_master.copy()

if phase:
    df = df[df["Phase"].isin(phase)]
if type_req:
    df = df[df["Type_exigence"].isin(type_req)]

st.dataframe(df)
