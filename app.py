import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

st.title("🎬 Movie Recommender System")

if not os.path.exists("model/movie_list.pkl") or not os.path.exists("model/similarity.pkl"):
    st.error("Model files missing in /model folder.")
    st.stop()

movies = pickle.load(open("model/movie_list.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))

movie_list = movies["title"].values
selected_movie = st.selectbox("Choose a movie:", movie_list)

if st.button("Recommend"):
    idx = movies[movies["title"] == selected_movie].index[0]
    distances = similarity[idx]
    top_movies = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    st.subheader("Top 5 Recommendations:")
    for i in top_movies:
        st.write(movies.iloc[i[0]].title)
