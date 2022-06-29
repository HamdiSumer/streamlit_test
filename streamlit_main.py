import streamlit as st


st.title("Strength Prediction")

st.header("Configurations:", anchor=None)

st.subheader("Feature Database:")

options = st.multiselect(
    "Select which features to use while training the model",
    [
        "K2O",
        "Al2O3",
        "Freelime",
        "SO3",
        "Fe2O3" "Na2O",
        "Le Chatelier",
        "Cl",
        "45mm",
        "Insoluble Residue",
        "Water Demand",
        "Initial Setting Time",
        "Specific Gravity",
        "CaO",
        "LOI",
        "MgO",
        "Blaine",
        "SiO2",
        "Type",
        "S.M",
        "Total",
        "Date of Sample",
        "EQ",
        "32mm",
        "90mm" "C3A",
        "C2S",
        "C3S",
        "H.M",
        "Al.M",
        "LSF",
        "L.faz",
    ],
    [
        "K2O",
        "Al2O3",
        "Freelime",
        "SO3",
        "Fe2O3" "Na2O",
        "Le Chatelier",
        "Cl",
        "45mm",
        "Insoluble Residue",
        "Water Demand",
        "Initial Setting Time",
        "Specific Gravity",
        "CaO",
        "LOI",
        "MgO",
        "Blaine",
        "SiO2",
        "Type",
    ],
)

# st.write("You selected:", options)
