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


# Neue Funktion find_movie_by_title hinzugefügt
def find_movie_by_title(title, movies):
    """
    Sucht nach einem Film basierend auf einem Teil des Titels und gibt die movieId und den Titel des am besten
    passenden Films zurück.
    """
    # Bereinige den eingegebenen Titel
    cleaned_title = clean_title(title)
    # Nutze die vorhandene Suchfunktionalität, um die Ähnlichkeit basierend auf dem bereinigten Titel zu finden
    vectorizer, tfidf_matrix = initialize_search(movies)
    similar_movies = search_movies(cleaned_title, vectorizer, tfidf_matrix, movies)
    if not similar_movies.empty:
        # Nimm den am besten passenden Film (ersten Eintrag nach der Sortierung)
        top_match = similar_movies.iloc[0]
        return top_match['movieId'], top_match['title']
    else:
        return None, None
