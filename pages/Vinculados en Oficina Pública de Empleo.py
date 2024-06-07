import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.sidebar.title("Filtros de Empleo")

logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)
st.title("Vinculados en Oficina Pública de Empleo")

df = pd.read_csv('datasets/vinculados_en_oficina_publica_de_empleo.csv')

municipios = sorted(df['municipio'].unique())
sexos = sorted(df['sexo'].unique())
niveles_educativos = sorted(df['máximo_nivel_educativo_alcanzado'].unique())
tipos_contrato = sorted(df['tipo_de_contrato'].unique())

# Filtro por Municipio y Sexo
st.subheader("Filtro por Municipio y Sexo")
selected_municipio = st.selectbox("Selecciona un Municipio:", municipios)
selected_sexo = st.selectbox("Selecciona un Sexo:", sexos)

filtered_df1 = df[(df['municipio'] == selected_municipio) & (df['sexo'] == selected_sexo)]
st.write(filtered_df1)

# Filtro por Nivel Educativo y Tipo de Contrato
st.subheader("Filtro por Nivel Educativo y Tipo de Contrato")
selected_nivel_educativo = st.selectbox("Selecciona un Nivel Educativo:", niveles_educativos)
selected_tipo_contrato = st.selectbox("Selecciona un Tipo de Contrato:", tipos_contrato)

filtered_df2 = df[(df['máximo_nivel_educativo_alcanzado'] == selected_nivel_educativo) & (df['tipo_de_contrato'] == selected_tipo_contrato)]
st.write(filtered_df2)
