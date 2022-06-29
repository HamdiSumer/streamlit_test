import streamlit as st


st.title("Strength Prediction")

st.header("Configurations:", anchor=None)

st.subheader("Feature Database:")

st.markdown("Select which features to use while training the model")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.write("You selected:", options)
