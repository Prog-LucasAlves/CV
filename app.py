import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Lucas Alves.
##### :email: *lucasalves_taz@hotmail.com*
##### :telephone_receiver: *(24) 9 92385509*
''')

image = Image.open('./image/cv.png')
st.image(image, width=150)

st.markdown('## :clipboard: Resumo', unsafe_allow_html=True)
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
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)

#####################


st.markdown('''
## :mortar_board: Formação Acadêmica
''')

txt('**Ciência de Dados** - Faculdade: Cruzeiro do Sul', '')
st.markdown('''
- Conclusão - 06/2022
''')
image = Image.open('./image/Diploma_rotated_page-0001.jpg')
st.image(image, width=300)

#####################
st.markdown('''
## :memo: Cursos de Aperfeiçoamento
''')

txt('**SQL para Data SCIENCE**', '')
st.markdown('''
- DSA - DATA SCIENCE ACADEMY
''')
image = Image.open('./image/DSA_Certificado_SQL_para_analise_de_Dados.jpg')
st.image(image, width=300)

txt('**Python para Análise de Dados**', '')
st.markdown('''
- DSA - DATA SCIENCE ACADEMY
''')
image = Image.open('./image/DSA_Certificado_Python_para_analise _de_Dados.jpg')
st.image(image, width=300)

txt('**Análise de Dados com Microsoft Power BI e Clínica de BI**', '')
st.markdown('''
- DSA - DATA SCIENCE ACADEMY
''')
image = Image.open('./image/DSA_Certificado_Power_BI_para_analise_de_Dados.jpg')
st.image(image, width=300)

txt('**Microsoft Power BI Para Data Science, Versão 2.0**', '')
st.markdown('''
- DSA - DATA SCIENCE ACADEMY
''')
image = Image.open('./image/Power_BI_Fundamentos.jpg')
st.image(image, width=300)

txt('**Python Fundamentos para Análise de Dados 3.0**', '')
st.markdown('''
- DSA - DATA SCIENCE ACADEMY ''')
image = Image.open('./image/Python_Fundamentos.jpg')
st.image(image, width=300)

txt('**Introdução a Engenharia de Dados**', '')
st.markdown('''
- DIGITAL INNOVATION ON
''')
image = Image.open('./image/Digital_One_Introdução_a_Engenharia_de_Dados.jpg')
st.image(image, width=300)

txt('**BOOTCAMP - Engenharia de Dados**', '')
st.markdown('''
- HOW BOOTCAMPS
''')
image = Image.open('./image/How_Eng_Dados_0.jpg')
st.image(image, width=300)
image = Image.open('./image/How_Eng_Dados_1.jpg')
st.image(image, width=300)

txt('**Python - Básico**', '')
st.markdown('''
- SEMANTIX ACADEMY
''')
image = Image.open('./image/Python – Básico-Lucas Alves.jpg')
st.image(image, width=300)

txt('**Estatística Descritiva**', '')
st.markdown('''
- SEMANTIX ACADEMY
''')
image = Image.open('./image/Estatística Descritiva-Lucas Alves.jpg')
st.image(image, width=300)

txt('**Leitura e Excrita de Dados**', '')
st.markdown('''
- SEMANTIX ACADEMY
''')
image = Image.open('./image/Leitura e Escrita de Dados-Lucas Alves.jpg')
st.image(image, width=300)

txt('**Pyspark - Básico**', '')
st.markdown('''
- SEMANTIX ACADEMY
''')
image = Image.open('./image/Pyspark - Básico-Lucas Alves.jpg')
st.image(image, width=300)

txt('**Machine Learning - Básico**', '')
st.markdown('''
- SEMANTIX ACADEMY
''')
image = Image.open('./image/Machine Learning - Básico-Lucas Alves.jpg')
st.image(image, width=300)


#####################
st.markdown('''
## :star: Habilidades
''')
txt3('Programming', '`Python`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`, `Excel`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Web development', '`Flask`')
txt3('Model deployment', '`streamlit`, `Heroku`')

#####################
st.markdown('''
## :computer: Mídias Sociais
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/lucasalves-ast/')
txt2('GitHub', 'https://github.com/Prog-LucasAlves/dados_financeiros_b3')
txt2('Medium', 'https://medium.com/@alveslucastaz')
