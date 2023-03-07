import pandas as pd
import numpy as np
import streamlit as st
import codecs
import re

DATA_URL= 'https://raw.githubusercontent.com/yoloogroth/Streamlit/master/citibike-tripdata.csv'
COLUMNA = 'started_at'

st.markdown("<h1 style='text-align: center; color: black;'>TRAVELING BY BIKE</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Yolotzin Groth Hernandez</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>zs20020311@estudiantes.uv.mx</h4>", unsafe_allow_html=True)
sidebar = st.sidebar


@st.cache
def cargar_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, encoding_errors='ignore')
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[COLUMNA] = pd.to_datetime(data[COLUMNA])
    return data
st.sidebar.image('https://raw.githubusercontent.com/yoloogroth/Streamlit/master/WhatsApp%20Image%202023-03-02%20at%2011.18.11%20AM.jpeg')

checkbox_data = sidebar.checkbox("Mostrar todos los datos")
if checkbox_data:
    estado = st.text('Cargando...')
    data = cargar_data(500)    
    estado.text("¡Cargado! (usando st.cache)")
    st.subheader('Todos los datos')
    st.dataframe(data)

checkbox_hora = sidebar.checkbox("Mostrar los datos por hora")
if checkbox_hora:
    estado = st.text('Cargando...')
    data = cargar_data(500)
    estado.text("¡Cargado! (usando st.cache)")
    st.subheader('Numero de recorridos por hora')
    values = np.histogram(data[COLUMNA].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(values)


filtro_hora = sidebar.slider('HORA', 0, 23, 17)
if filtro_hora:
    estado = st.text('Cargando...')
    data = cargar_data(500)
    estado.text("¡Cargado! (usando st.cache)")
    data_rename = data.rename(columns = {'start_lat': 'lat', 'start_lng': 'lon'}, inplace = False)
    filtrar_data = data_rename[data_rename[COLUMNA].dt.hour == filtro_hora]
    st.subheader('Mapa de los recorridos iniciados a las %s:00' % filtro_hora)
    st.map(filtrar_data)