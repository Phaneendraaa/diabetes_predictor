import streamlit as st
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open("C:/Users/nagap/Downloads/diabetes_model.sav",'rb'))
# Title and description of the app
st.title("Diabetes Prediction App")
st.write("Enter the required values to predict if a person has diabetes.")

# Input features
pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1)
glucose = st.number_input('Glucose Level', min_value=0, max_value=200, step=1)
blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=150, step=1)
skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, step=1)
insulin = st.number_input('Insulin Level', min_value=0, max_value=900, step=1)
bmi = st.number_input('BMI (Body Mass Index)', min_value=0.0, max_value=70.0, step=0.1)
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, step=0.01)
age = st.number_input('Age', min_value=1, max_value=120, step=1)

# Button to make prediction
if st.button("Predict"):
    # Prepare input data as an array
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

    # Predict using the loaded model
    prediction = model.predict(input_data)

    # Display the result
    if prediction[0] == 1:
        st.error("The person is likely to have diabetes.")
    else:
        st.success("The person is unlikely to have diabetes.")

# To run this app, use the command in terminal:
# streamlit run app.py
