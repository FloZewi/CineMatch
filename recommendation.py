import pandas as pd

from search import search_movies
from data_utils import clean_title
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_movie_tags(movie_id, tags_df):
    """Ruft alle Tags ab, die zu einer bestimmten movieId gehören."""
    tags = tags_df[tags_df['movieId'] == movie_id]['tag'].tolist()
    return tags


# Hinzufügen von Tags zu den Empfehlungen
def add_tags_to_recommendations(recommendations, tags_data):
    """Fügt den empfohlenen Filmen Tags hinzu."""
    recommendations = recommendations.copy()  # Eine Kopie machen, um SettingWithCopyWarning zu vermeiden
    recommendations['tags'] = recommendations['movieId'].apply(lambda x: get_movie_tags(x, tags_data))
    return recommendations


def create_tag_matrix(tags_df):
    """Erstellt eine Matrix aus Film-IDs und zugehörigen Tags."""
    tags_df['tag'] = tags_df['tag'].fillna('')  # NaN-Werte durch leere Strings ersetzen
    tags_df['tag'] = tags_df['tag'].astype(str)  # Erzwingen, dass alle Tags als Strings behandelt werden
    tags_combined = tags_df.groupby('movieId')['tag'].apply(lambda x: ' '.join(x)).reset_index()
    return tags_combined


def calculate_similarity(tags_combined):
    """Berechnet die Ähnlichkeit zwischen Filmen basierend auf Tags."""
    vectorizer = CountVectorizer()
    tag_matrix = vectorizer.fit_transform(tags_combined['tag'])
    similarity = cosine_similarity(tag_matrix, tag_matrix)
    return similarity, tags_combined['movieId']


def get_similar_movies(movie_id, similarity, movie_ids):
    """Gibt Filme zurück, die ähnliche Tags wie der gegebene Film haben."""
    index = movie_ids[movie_ids == movie_id].index[0]
    similar_movies = list(enumerate(similarity[index]))
    similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:11]  # Top 10 ähnliche Filme
    similar_movie_ids = [movie_ids.iloc[i[0]] for i in similar_movies]
    return similar_movie_ids


def refine_recommendations(movie_id, movies, tags_data):
    """Verfeinert Empfehlungen basierend auf tag-Ähnlichkeit."""
    tags_combined = create_tag_matrix(tags_data)
    if tags_combined is not None:
        similarity, movie_ids = calculate_similarity(tags_combined)
        similar_movie_ids = get_similar_movies(movie_id, similarity, movie_ids)
        refined_recommendations = movies[movies['movieId'].isin(similar_movie_ids)].copy()
        refined_recommendations['clean_title'] = refined_recommendations['title'].apply(clean_title)
        return refined_recommendations[['clean_title', 'movieId']]
    else:
        # Geeignete Fehlerbehandlung oder Rückgabe eines leeren DataFrames
        return pd.DataFrame()


# Empfehlungsfunktion
def generate_recommendations(movie_id, movies, ratings, tags_data, vectorizer, tfidf_matrix):
    # Suche nach ähnlichen Filmen basierend auf movie_id
    movie_title = movies[movies['movieId'] == movie_id]['title'].iloc[0]
    recommended_movies = search_movies(movie_title, vectorizer, tfidf_matrix, movies)

    # Berechnen der durchschnittlichen Bewertung für jeden Film
    average_ratings = ratings.groupby('movieId')['rating'].mean().rename('average_rating')

    # Zusammenführen der Empfehlungen mit den durchschnittlichen Bewertungen
    recommended_movies_with_ratings = recommended_movies.merge(average_ratings, left_index=True, right_on='movieId')

    # Bereinige Titel, um das Jahr zu entfernen
    recommended_movies_with_ratings['clean_title'] = recommended_movies_with_ratings['title'].apply(clean_title)

    # Wähle nur die Spalten 'movieId', 'clean_title' und 'average_rating' zur Ausgabe
    final_recommendations = recommended_movies_with_ratings[['movieId', 'clean_title', 'average_rating']]

    # Tags zu den Empfehlungen hinzufügen
    final_recommendations_with_tags = add_tags_to_recommendations(final_recommendations.copy(), tags_data)

    # Entfernt 'movieId' Spalte, weil nicht in der finalen Ausgabe erwünscht
    final_recommendations_with_tags = final_recommendations_with_tags[['clean_title', 'average_rating', 'tags']]

    return final_recommendations_with_tags
