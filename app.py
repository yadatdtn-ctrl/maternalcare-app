# MaternalCare AI — Main App

import streamlit as st
from bmi_module import calculate_bmi, classify_bmi
from edd_module import calculate_edd, calculate_weeks

st.title("Maternalcare AI")
st.write("A smart health assistant for pregnant women")
st.divider()

tab1, tab2, tab3 = st.tabs(["BMI Calculator", "Delivery Date", "Risk Prediction"])

with tab1:
    st.header("BMI Calculator")
    weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
    height = st.number_input("Height (cm)", min_value=1.0, value=165.0)

    if st.button("Calculate BMI"):
        height_m = height / 100
        bmi = calculate_bmi(weight, height_m)
        category = classify_bmi(bmi)
        st.metric("Your BMI", bmi)
        st.success(f"Category: {category}")

with tab2:
    st.header("Delivery Date")
    from datetime import date
    Imp = st.date_input("Last Menstrual Period (LMP)", value=date(2025, 9, 1))

    if st.button("Calculate Delivery Date"):
        edd = calculate_edd(Imp)
        weeks = calculate_weeks(Imp)
        st.metric("Expected Delivery Date", edd.strftime("%d %B %Y"))
        st.metric("Weeks Pregnant", f"Week {weeks}")
        



