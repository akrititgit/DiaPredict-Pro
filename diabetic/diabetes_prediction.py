# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:49:07 2022

@author: dell
"""
import numpy as np
import pickle
import streamlit as st


loaded_model=pickle.load(open('C:/Users/dell/Desktop/diabetic/trained_model.sav','rb'))


def predict(input_data):
    
    
    #changing the input data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)
    
    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0]==0:
      return "the user is not diabetic"
    else:
      return "the user is diabetic"
  
def main():
    
    #giving a title
    st.title("Diabetes Prediction Web App")
    
    #getting the input data from the user
    
    Pregnancies = st.text_input("enter no.of pregnancies")
    Glucose = st.text_input("enter glucose level")
    BloodPressure= st.text_input("enter blood pressure value")
    skinthickness= st.text_input("enter skinthickness") 
    Insulin = st.text_input("enter insulin level")
    BMI = st.text_input("enter BMI")
    DiabetesPedigreeFucntion = st.text_input("enter DPF")
    Age= st.text_input("enter your age")
    
    
    #code for prediction
    diagonosis=''
    if st.button("Diabetes Test Result"):
        diagonosis=predict([Pregnancies,Glucose,BloodPressure,skinthickness,Insulin,BMI,DiabetesPedigreeFucntion,Age
        ])
    st.success(diagonosis)
    
if __name__=='__main__':
    main()