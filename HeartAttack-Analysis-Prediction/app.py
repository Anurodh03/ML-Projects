import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image



pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)



def predict_note_authentication(age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall):
   
   
    prediction=classifier.predict([[age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]])
    return prediction[0]


def main():
    
    st.title("Heart Attack Prediction")
        
    age = st.text_input("age","Type Here")
    sex = st.text_input("sex","Type Here")
    cp = st.text_input("cp","Type Here")
    trtbps = st.text_input("trtbps","Type Here")
    chol = st.text_input("chol","Type Here")
    fbs = st.text_input("fbs","Type Here")
    restecg = st.text_input("restecg","Type Here")
    thalachh = st.text_input("thalachh","Type Here")
    exng = st.text_input("exng","Type Here")
    oldpeak = st.text_input("oldpeak","Type Here")
    slp = st.text_input("slp","Type Here")
    caa = st.text_input("caa","Type Here")
    thall = st.text_input("thall","Type Here")



    if sex == "male":
       sex=1
    else:
       sex=0


        
    result=""
    if st.button("Predict"):
       result=predict_note_authentication(age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall)
       if result == 0:
          result = "You have high chances of Heart Attack :("
       else:
          result = "Hurray, You are Healthy"
       
    st.success(result)


if __name__=='__main__':
    main()

