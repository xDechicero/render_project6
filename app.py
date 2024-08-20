import pandas as pd
import streamlit as st
import plotly.express as px

datos = pd.read_csv('vehicles_us.csv')
#print(datos.head())

st.header('Graficos de odometros de US')

build_histogram = st.checkbox('Construir un histograma')

build_dispercion = st.checkbox('Construir un grafico de dispercion')

if build_histogram:
    st.write('creacion de histograma de odometros de los autos ')

    fig=px.histogram(datos, x='odometer')

    st.plotly_chart(fig)

if build_dispercion:
    st.write('creacion de grafico de dispercion de odometros de los autos ')

    fig2 = px.scatter(datos, x="odometer", y="price") # crear un gráfico de dispersión

    st.plotly_chart(fig2)