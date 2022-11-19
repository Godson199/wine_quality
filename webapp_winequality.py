import base64
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import pickle  

st.markdown(f'<h1 style="color:#33ff33; font-size:60px;">{"Wine Quality Prediction "}</h1>', unsafe_allow_html=True)

# loading model
pickle_in = open("wine_quality_model", "rb")
model = pickle.load(pickle_in)

# side_bar to navigate
with st.sidebar:
    selected = option_menu("Multiple Model Prediction",
    ["RandomForestClassifier",
    "LogisticRegression",
    "DecisionTreeClassifier"])


# making prediction with the model
def predict_wine_quality(fixed_acidity, volatile_acidity, citric_acid, residual_sugar,chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,pH, sulphates, alcohol):

    prediction = model.predict(np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,pH, sulphates, alcohol]], dtype=object))
    return prediction
def main():
# building interface with streamlit
    if (selected == "RandomForestClassifier"):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            fixed_acidity = st.text_input("fixed acidity", "")
        with col2:
            volatile_acidity = st.text_input("volatile acidity", "")

        with col3:
            citric_acid = st.text_input("citric acid", "")
        
        with col4:
            residual_sugar = st.text_input("residual sugar", "")
        
        with col1:
            chlorides = st.text_input("chlorides", "")
        
        with col2:
            free_sulfur_dioxide = st.text_input("free sulfur dioxide", "")
        
        with col3:
            total_sulfur_dioxide = st.text_input("total sulfur dioxide", "")

        with col4:
            density = st.text_input("density", "")

        with col1:
            pH = st.text_input("pH", "")
        with col2:
            sulphates = st.text_input("sulphates", "")
        with col3:
            alcohol = st.text_input("alcohol", "")

        result=""
        if st.button("Wine Quality"):
            result = predict_wine_quality(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,
            chlorides,free_sulfur_dioxide, total_sulfur_dioxide,density, pH, sulphates, alcohol)
        
            if result == 1:
                st.success("Good Wine Quality ")
            elif result ==0:
                st.success("Bad Wine Quality!")
        else:
            st.success("Incorrect Input")  

    
    # Next Model

    
    if st.button("About"):
        st.text("Built by: Izuogu Chibuzor Godson")


if __name__== "__main__":
    main()
