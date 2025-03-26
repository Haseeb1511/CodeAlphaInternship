import streamlit as st
import pandas as pd
import pickle

with open("heart_disease_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Heart Disease Prediction")

st.sidebar.header("ENter Patient Data")

def user_input():   
    age = st.sidebar.slider("chose your age",0,100)
    sex = st.sidebar.selectbox("Sex (0=>male and 1=>female)",[0,1])
    cp = st.sidebar.slider("Chose your cp",0,3,1)
    trestbps = st.sidebar.slider("Chose your bps",80,200,120)
    chol = st.sidebar.slider("chose your chlosteral level",126,564,126)
    fbs = st.sidebar.selectbox("Chose your fbs",[0,1])
    restecg = st.sidebar.selectbox("Chose your restecg",[0,1,2])
    thalach = st.sidebar.slider('chose your thaach',71,202,120 )
    exang = st.sidebar.selectbox('Chose your exang',[0,1])
    oldpeak = st.sidebar.slider("Chose oldpeak value",0.0,6.2,1.0)
    slope = st.sidebar.selectbox("Chose your slope",[0,1,2])
    ca =st.sidebar.slider("CHose your ca",0,4,2)
    thal = st.sidebar.slider("chose your thal level",0,3,1)

    data = {
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps, "chol": chol,
        "fbs": fbs, "restecg": restecg, "thalach": thalach, "exang": exang,
        "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal
    }
    return pd.DataFrame([data])

input_data = user_input()

if st.button("Predict"):
    prediction = model.predict(input_data)
    

    st.subheader("Prediction result is : ")
    if prediction[0]==1:
        st.error("High risk of heart disease")
    else:
        st.success("Good Health")
    