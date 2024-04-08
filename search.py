import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re


# Funktion zum Bereinigen von Filmtiteln
def clean_title(title):
    # Entfernt alles außer Buchstaben und Zahlen und ersetzt es durch Leerzeichen
    return re.sub(pattern='[^a-zA-Z0-9 ]', repl='', string=title)


# Funktion zum Laden von Daten aus einer CSV-Datei
def load_data():
    data = pd.read_csv("movies.csv")
    # Bereinigen der Titel und Hinzufügen einer neuen Spalte
    data['clean_title'] = data['title'].apply(clean_title)
    return data


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


# Pfad zur CSV-Datei
csv_file_path = 'movies.csv'
movies_data = load_data()

# Suchfunktionalität initialisieren
vectorizer, tfidf_matrix = initialize_search(movies_data)

# Durchführen einer Suche nach einem Beispiel-Filmtitel
search_query = "Toy Story"
search_results = search_movies(search_query, vectorizer, tfidf_matrix, movies_data)

# Ergebnisse anzeigen
print(f"Suchergebnisse für '{search_query}':")
print(search_results[['title', 'clean_title']])
