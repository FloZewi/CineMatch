from search import search_movies
from data_utils import clean_title


# Empfehlungsfunktion
def generate_recommendations(movie_id, movies, ratings, vectorizer=None, tfidf_matrix=None):
    # Suche nach ähnlichen Filmen basierend auf movie_id
    movie_title = movies[movies['movieId'] == movie_id]['title'].iloc[0]
    recommended_movies = search_movies(movie_title, vectorizer, tfidf_matrix, movies)

    # Berechnen der durchschnittlichen Bewertung für jeden Film
    average_ratings = ratings.groupby('movieId')['rating'].mean().rename('average_rating')

    # Zusammenführen der Empfehlungen mit den durchschnittlichen Bewertungen
    recommended_movies_with_ratings = recommended_movies.merge(average_ratings, left_index=True, right_on='movieId')

    # Bereinige Titel, um das Jahr zu entfernen
    recommended_movies_with_ratings['clean_title'] = recommended_movies_with_ratings['title'].apply(clean_title)

    # Wähle nur die Spalten 'clean_title' und 'average_rating' zur Ausgabe
    final_recommendations = recommended_movies_with_ratings[['clean_title', 'average_rating']]

    return final_recommendations
