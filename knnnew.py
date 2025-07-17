import streamlit as st
import pickle

with open("knn.pkl","rb") as file:
    model=pickle.load(file)
age=st.number_input("Enter Age")
salary=st.number_input("Salary")
exp=st.number_input("Experience (Years)")
dept=st.number_input("Enter Department Number")

pred=model.predict([[age,salary,exp,dept]])
if st.button('Analyse'):
    if pred==1:
        st.success("You are doing good")
    else:
        st.warning("Chances of layoff")
