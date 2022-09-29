import streamlit as st
import joblib
model = joblib.load('MOVIES')
st.title('MOVIE CATEGORY')
ip = st.text_input('Enter the movie name')
op = model.predict([ip])
if st.button('predict'):
  st.title(op[0])
