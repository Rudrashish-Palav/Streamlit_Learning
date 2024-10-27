import streamlit as st
import pandas as pd 

st.title("Streamlit Text Input")

age = st.slider("Select your age :", 0,100,25)
st.write(f"Your age is {age}")

name = st.text_input("Enter your name :")
if name : 
    st.write(f"Hello, {name}")

options = ["Python", " Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favourite language", options)
st.write(f"You've selected {choice}")

df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]},
                  index=['falcon', 'dog', 'spider', 'fish'])
st.write(df)

uploaded_file = st.file_uploader("Chose a CSV file", type = 'csv')
if uploaded_file is not None : 
     df = pd.read_csv(uploaded_file)
     st.write(df)

     