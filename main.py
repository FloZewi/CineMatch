from data_preparation import prepare_movies_data
from search import initialize_search, search_movies
from recommendation import generate_recommendations
from data_utils import load_data


def main():
    # Lade die Datensätze
    print("Lade Filmdaten...")
    movie_filepath = 'movies.csv'
    ratings_filepath = 'ratings.csv'

    # Daten vorbereiten
    movies_data = prepare_movies_data(movie_filepath)
    ratings_data = load_data(ratings_filepath)

    if movies_data is not None or ratings_data is not None:
        vectorizer, tfidf_matrix = initialize_search(movies_data)

        # Durchführen einer Suche (Beispiel)
        search_query = "Toy Story"
        print(f"Suchergebniss für '{search_query}':")
        search_results = search_movies(search_query, vectorizer, tfidf_matrix, movies_data)
        print(search_results[['title', 'clean_title']])

        # Generieren Filmempfehlungen (Beispiel)
        movie_id_to_search = 16     # movie_id
        print(f"\nEmpfehlungen für Film ID {movie_id_to_search}:")
        recommendations = generate_recommendations(movie_id_to_search, movies_data, ratings_data, vectorizer,
                                                   tfidf_matrix)
        print(f"Empfehlungen für Film ID {movie_id_to_search}: {recommendations[['title', 'clean_title',
                                                                                 'average_rating']]}")


if __name__ == "__main__":
    main()
