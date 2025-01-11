import streamlit as st
URL=st.text_input('Image URL')
if st.button('View image'):
 
 st.image(URL)