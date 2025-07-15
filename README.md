# 🎬 Movie Recommendation System

[![Streamlit App](https://img.shields.io/badge/Live‑Demo-Streamlit‑Cloud-green?logo=streamlit)](https://movie-recommender-streamlit-pranshigupta7275.streamlit.app/)
[![License](https://img.shields.io/badge/license-MIT-blue)](#license)

Content‑based movie recommender that matches titles by **TF‑IDF** vectors of plot overviews and ranks them with **cosine similarity**.  
The app fetches poster images via the TMDB API and serves real‑time recommendations in a lightweight Streamlit UI.

---

## ✨ Features
| Feature | Details |
|---------|---------|
| **TF‑IDF + Cosine Similarity** | Generates a 5‑nearest‑neighbour list for 5 000+ movies. |
| **Poster Integration** | Calls TMDB API to display high‑quality posters beside each recommendation. |
| **Compressed Similarity Matrix** | Uses `float16` + `joblib` to keep similarity file < 25 MB (GitHub‑safe). |
| **Deployed on Streamlit Cloud** | One‑click shareable URL, CI/CD via GitHub. |

---

## 🚀 Quick Start

```bash
# clone repo
git clone https://github.com/Pranshigupta7275/Movie-Recommender-streamlit.git
cd Movie-Recommender-streamlit

# install dependencies (in a venv)
pip install -r requirements.txt

# add your TMDB key (either .env or secrets.toml)
export TMDB_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# run locally
streamlit run app.py
