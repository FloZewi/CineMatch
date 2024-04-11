from data_preparation import prepare_movies_data
from search import initialize_search
from recommendation import generate_recommendations, refine_recommendations, combine_recommendations
from data_utils import load_data, load_tags_data


def main():
    # Lade die Datensätze
    print("Lade Filmdaten...")
    movie_filepath = 'movies.csv'
    ratings_filepath = 'ratings.csv'
    tags_filepath = 'tags.csv'

    # Daten vorbereiten
    movies_data = prepare_movies_data(movie_filepath)
    ratings_data = load_data(ratings_filepath)
    tags_data = load_tags_data(tags_filepath)

    if movies_data is not None or ratings_data is not None:
        vectorizer, tfidf_matrix = initialize_search(movies_data)

        # Durchführen einer Suche (Beispiel)
        # search_query = "Toy Story"
        # print(f"Suchergebnisse für '{search_query}':")
        # search_results = search_movies(search_query, vectorizer, tfidf_matrix, movies_data)
        # print(search_results[['title', 'clean_title']])

        # Generieren Filmempfehlungen (Beispiel)
        movie_id_to_search = 16     # movie_id
        # print(f"\nEmpfehlungen für Film ID {movie_id_to_search}:")
        # recommendations = generate_recommendations(movie_id_to_search, movies_data, ratings_data, tags_data,
        #                                           vectorizer, tfidf_matrix)
        # print(f"Empfehlungen für Film ID {movie_id_to_search}:
        # {recommendations[['clean_title', 'average_rating']]}\n")

        # Verwenden von refine_recommendations, um tag-basierte Empfehlungen zu generieren
        # print(f"\nTag-basierte Empfehlungen für Film ID {movie_id_to_search}:")
        # tag_based_recommendations = refine_recommendations(movie_id_to_search, movies_data, tags_data)

        # Ausgabe entsprechend der Struktur der Daten anpassen
        # print(tag_based_recommendations[['clean_title', 'movieId']].head())

        # Generieren von Empfehlungen mit beiden Methoden
        recs_general = generate_recommendations(movie_id_to_search, movies_data, ratings_data, tags_data, vectorizer,
                                                tfidf_matrix)
        recs_tags = refine_recommendations(movie_id_to_search, movies_data, tags_data)

        # Ausgabe der general und tag-basierten Empfehlungen vor der Kombination
        # print(f"Allgemeine Empfehlungen: {recs_general[['clean_title', 'average_rating']].head()}\n")
        # print(f"Tag-basierte Empfehlungen: {recs_tags[['clean_title', 'movieId']].head()}\n")

        # Kombinieren der Empfehlungen
        combined_recs = combine_recommendations(recs_general, recs_tags)
        print("Kombinierte Empfehlungen:")
        print(combined_recs.head())


if __name__ == "__main__":
    main()
