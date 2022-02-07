import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Lucas Alves.
##### *lucasalves_taz@hotmail*
##### *(24) 9 92385509* 
''')

image = Image.open('./cv.jpg')
st.image(image, width=150)

st.markdown('## Resumo', unsafe_allow_html=True)
st.info('''
- Estudante de Ciência de dados & Fan de Python/SQL.
- Sempre na busca de aprender algo novo.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

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
## Formação Acadêmica
''')

txt('**Ciência de Dados**','Cruzeiro do Sul')
st.markdown('''
- Conclusão - 06/2022
''')

#####################
st.markdown('''
## Texto 05
''')

txt('** Texto 06','1')
st.markdown('''
- Texto 07
''')

#####################
st.markdown('''
## Habilidades
''')
txt3('Programming', '`Python`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')

#####################
st.markdown('''
## Mídias Sociais
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/lucasalves-ast/')
txt2('GitHub', 'https://github.com/Prog-LucasAlves/dados_financeiros_b3')
