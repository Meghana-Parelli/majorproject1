import streamlit as st
import joblib
model_nb = joblib.load('MOVIES')
st.title('MOVIES') #creates a title in web app
ip = st.text_input('Enter Movie name:') #creates a text box in web app
op = model_nb.predict([ip])
if st.button('Predict'):
  st.title(op[0])

  
  
  
  
  
  
  
