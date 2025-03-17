"""Aplicación para mostrar información de anuncios de autos en EEUU"""
import streamlit as st
import pandas as pd
import plotly.express as px

autos = pd.read_csv('vehicles_us.csv')

st.header('Información de los anuncios de autos en EEUU')

boton_hist=st.button('Crear histograma')

if boton_hist:
    st.write('Histograma de precios x distancia')
    fig = px.histogram(autos, x='odometer', y='price', color='type')
    st.plotly_chart(fig, use_container_width=True)

opcion_scatter=st.checkbox('Crear Dispersión', value=True)

if opcion_scatter:
    st.write('Dispersión de precios x año')
    fig = px.scatter(autos, x='model_year', y='price', color='type')
    st.plotly_chart(fig, use_container_width=True)