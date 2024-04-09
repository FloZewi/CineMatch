import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data_utils import clean_title


# Initialisiert die Suchfunktionalität
def initialize_search(movies):
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    local_tfidf_matrix = vectorizer.fit_transform(movies['clean_title'])
    return vectorizer, local_tfidf_matrix


# Suchfunktion, um Filme basierend auf einem gegebenen Titel zu finden
def search_movies(query, vectorizer, tfidf_matrix, movies):
    query_clean = clean_title(query)
    query_vec = vectorizer.transform([query_clean])
    similarity = cosine_similarity(query_vec, tfidf_matrix).flatten()
    indices = np.argsort(similarity)[-20:]  # Die Top-20-Indizes
    return movies.iloc[indices][::-1]  # Filme mit den höchsten Ähnlichkeitswerten
