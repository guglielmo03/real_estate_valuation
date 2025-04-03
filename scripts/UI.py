import os
import sys
sys.path.append(os.path.abspath(".."))
from src import config
import streamlit as st
import numpy as np
import pickle

# Load the models and vectorizer
with open(os.path.join(config.MODELS_PATH, "random_forest_complete.pickle"), "rb") as file:
    rfComplete = pickle.load(file)

with open(os.path.join(config.MODELS_PATH, "random_forest_lat_long.pickle"), "rb") as file:
    rfLatLong = pickle.load(file)

with open(os.path.join(config.MODELS_PATH, "random_forest_not_lat_long.pickle"), "rb") as file:
    rfNotLatLong = pickle.load(file)

st.title("Previsione costo casa")

selectedModel = st.selectbox(
         'Quali dati vorresti immetere per prevedere il prezzo della casa?',
         ('Latitudine e Longitudine', 'Età dell’immobile, distanza dalla stazione MRT più vicina e numero di minimarket nelle vicinanze',
          "Tutti quelli possibili"))

if selectedModel == "Latitudine e Longitudine":
    latitudine = st.number_input("Latitudine", min_value=-90.0, max_value=90.0, value=25.0, step=0.01)
    longitudine = st.number_input("Longitudine", min_value=-180.0, max_value=180.0, value=120.0, step=0.01)
elif selectedModel == "Età dell’immobile, distanza dalla stazione MRT più vicina e numero di minimarket nelle vicinanze":
    eta_immobile = st.number_input("Età dell'immobile (anni)", min_value=0, max_value=200, value=10)
    distanza_mrt = st.number_input("Distanza dalla stazione MRT più vicina (m)", min_value=0, value=10000, step=100)
    num_minimarket = st.number_input("Numero di minimarket nelle vicinanze", min_value=0, value=5)
else:
    latitudine = st.number_input("Latitudine", min_value=-90.0, max_value=90.0, value=25.0, step=0.01)
    longitudine = st.number_input("Longitudine", min_value=-180.0, max_value=180.0, value=120.0, step=0.01)
    eta_immobile = st.number_input("Età dell'immobile (anni)", min_value=0, max_value=200, value=10)
    distanza_mrt = st.number_input("Distanza dalla stazione MRT più vicina (m)", min_value=0, value=10000, step=100)
    num_minimarket = st.number_input("Numero di minimarket nelle vicinanze", min_value=0, value=5)

# Predict when button is clicked
if st.button("Prevedi costo casa"):
    if selectedModel == "Latitudine e Longitudine":
        X_input = np.array([[latitudine, longitudine]])
        prediction = rfLatLong.predict(X_input)[0]
    elif selectedModel == "Età dell’immobile, distanza dalla stazione MRT più vicina e numero di minimarket nelle vicinanze":
        X_input = np.array([[eta_immobile, distanza_mrt, num_minimarket]])
        prediction = rfNotLatLong.predict(X_input)[0]
    else:
        X_input = np.array([[latitudine, longitudine, eta_immobile, distanza_mrt, num_minimarket]])
        prediction = rfComplete.predict(X_input)[0]

    st.success(f"🏡 Valore stimato dell'immobile: **{prediction:.2f}** dollari per unità d'area")