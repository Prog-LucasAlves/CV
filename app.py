import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Lucas Alves, .
##### *Resume* 
''')

image = Image.open('./cv.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Texto 01
''')

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('** Texto 02','1')
st.markdown('''
- Texto 03
''')

txt('** Texto 04','1')
st.markdown('''
- Texto 05
''')

#####################
st.markdown('''
## Texto 05
''')

txt('** Texto 06','1')
st.markdown('''
- Texto 07
''')

txt('** Texto 08','1')
txt('** Texto 09','1')
txt('** Texto 10','1')
st.markdown('''
- Texto 11
''')

txt('** Texto 12','1')
st.markdown('''
- Texto 13
''')

txt('** Texto 14','1')
st.markdown('''
- Texto 15
''')

txt('** Texto 16','1')
st.markdown('''
- Texto 17
''')

txt('**Texto 18','1')
st.markdown('''
- Texto 19
''')

#####################
st.markdown('''
## Bioinformatics Tools
''')
txt4('Texto 20','1')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', '')
