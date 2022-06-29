import streamlit as st

st.title("Strength Prediction")

plant = st.selectbox(
     'Select Plant',
     ('Büyükçekmece Fabrikası', 'Çanakkale Fabrikası', 'Karçimsa Fabrikası', 'Ladik Fabrikası'))

date_initial = st.date_input(
     "From:",
     datetime.date(2022, 1, 1))

date_initial = st.date_input(
     "To:",
     datetime.date(2022, 1, 1))