from search import search_movies
from data_utils import clean_title


def get_movie_tags(movie_id, tags_df):
    """Ruft alle Tags ab, die zu einer bestimmten movieId gehören."""
    tags = tags_df[tags_df['movieId'] == movie_id]['tag'].tolist()
    return tags


# Hinzufügen von Tags zu den Empfehlungen
def add_tags_to_recommendations(recommendations, tags_data):
    """Fügt den empfohlenen Filmen Tags hinzu."""
    recommendations['tags'] = recommendations['movieId'].apply(lambda x: get_movie_tags(x, tags_data))
    return recommendations


# Empfehlungsfunktion
def generate_recommendations(movie_id, movies, ratings, tags_data, vectorizer=None, tfidf_matrix=None):
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
