import pandas as pd
import plotly
import plotly.express as px
import streamlit as st
import etl

st.title("Главная страница")


genres = etl.load_data('genres')
movies = etl.load_data('movies')
screenings = etl.load_data('screenings')
theaters = etl.load_data('theaters')


st.header("Таблица: Жанры")
st.dataframe(genres)

st.header("Таблица: Фильмы")
st.dataframe(movies)

st.header("Таблица: Сеансы")
st.dataframe(screenings)

st.header("Таблица: Театры")
st.dataframe(theaters)