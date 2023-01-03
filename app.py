import streamlit as st
import joblib
knn_model=joblib.load("bmi_model")
st.title("Weight Height based BMI classifier")
weight=st.slider("Weight of the person in kg",40,100,60)
height=st.slider("Height of the person in cm",140,190,160)
if st.button('PREDICT'):
  op=knn_model.predict([[weight,height]])
  st.subheader("The BMI class for the person with the above specified weight and height is: "+op[0])
