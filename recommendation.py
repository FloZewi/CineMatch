from search import initialize_search, search_movies
from data_preparation import clean_title, load_data


# Empfehlungsfunktion
def generate_recommendations(movie_id, movies, ratings):
    # Initialisieren Sie die Suchfunktionalität
    vectorizer, tfidf_matrix = initialize_search(movies)

    # Suche nach ähnlichen Filmen basierend auf movie_id
    movie_title = movies[movies['movieId'] == movie_id]['title'].iloc[0]
    recommended_movies = search_movies(movie_title, vectorizer, tfidf_matrix, movies)

    # Berechnen der durchschnittlichen Bewertung für jeden Film
    average_ratings = ratings.groupby('movieId')['rating'].mean().rename('average_rating')

    # Zusammenführen der Empfehlungen mit den durchschnittlichen Bewertungen
    recommended_movies_with_ratings = recommended_movies.merge(average_ratings, left_index=True, right_on='movieId')

    # Ergebnisse ausgeben
    print(f"Empfehlungen für den Film '{movie_title}':")
    print(recommended_movies_with_ratings[['title', 'clean_title', 'average_rating']])

    return recommended_movies_with_ratings


if __name__ == "__main__":
    # Laden der Datensätze
    movies_filepath = 'movies.csv'
    ratings_filepath = 'ratings.csv'
    movies_data = load_data("movies.csv")
    ratings_data = load_data("ratings.csv")

    # Bereinigen der Filmtitel
    movies_data['clean_title'] = movies_data['title'].apply(clean_title)

    # Generieren von Filmempfehlungen
    movie_id_to_search = 1  # Tatsächliche movie_id einsetzen
    recommendations = generate_recommendations(movie_id_to_search, movies_data, ratings_data)
