import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.write('''
# Lucas Alves - Estudante de Ciência de dados & Fan de Python.
##### *Resume* 
''')
image = Image.open('./cv.jpg')
st.image(image, width=150)