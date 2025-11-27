import streamlit as st
from dataset import df_master

st.title("IoT Monitor")

st.write("Relevés IoT fictifs : Monitoring Température / Fréquence")

data = {
    "Capteur": ["Température Frigo 01", "Frigo 02", "Salle Stockage"],
    "Température": ["7.2°C", "6.8°C", "20.5°C"],
    "Fréquence": ["Toutes les 10 min", "Toutes les 10 min", "Toutes les 60 min"]
}

import pandas as pd
st.dataframe(pd.DataFrame(data))
