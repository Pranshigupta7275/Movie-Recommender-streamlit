import pandas as pd, pickle, os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1) Load CSV you just uploaded
movies = pd.read_csv("tmdb_5000_movies.csv")[["id", "title", "overview"]]
movies.rename(columns={"id": "movie_id"}, inplace=True)
movies["overview"] = movies["overview"].fillna("")

# 2) TF‑IDF + cosine similarity
tfidf  = TfidfVectorizer(stop_words="english")
matrix = tfidf.fit_transform(movies["overview"])
similarity = cosine_similarity(matrix, matrix)

# 3) Save artefacts into /model
os.makedirs("model", exist_ok=True)
pickle.dump(movies,     open("model/movie_list.pkl", "wb"))
pickle.dump(similarity, open("model/similarity.pkl", "wb"))
print("✅  Saved: model/movie_list.pkl  &  model/similarity.pkl")
