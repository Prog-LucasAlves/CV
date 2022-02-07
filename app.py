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
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Chanin Nantasenamat</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

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
