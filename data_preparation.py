from data_utils import load_data, clean_title


# Lädt die Daten, bereinigt die Titel und fügt diese als neue Spalte hinzu
def prepare_movies_data(movies_filepath):
    movies_data = load_data(movies_filepath)
    if movies_data is not None:
        movies_data['clean_title'] = movies_data['title'].apply(clean_title)
    return movies_data
