import tkinter as tk
from tkinter import messagebox
from data_preparation import prepare_movies_data
from search import initialize_search, find_movie_by_title
from recommendation import generate_recommendations, refine_recommendations, combine_recommendations
from data_utils import load_data, load_tags_data


# Haupt-GUI-Klasse
class MovieRecommenderGUI:
    def __init__(self, root):
        self.result_text = None
        self.search_button = None
        self.title_entry = None
        self.root = root
        self.root.title("CineMatch: Dein persönlicher Filmempfehlungsgenerator")

        # Initialisiere die Daten
        self.movie_filepath = 'movies.csv'
        self.ratings_filepath = 'ratings.csv'
        self.tags_filepath = 'tags.csv'
        self.movies_data = prepare_movies_data(self.movie_filepath)
        self.ratings_data = load_data(self.ratings_filepath)
        self.tags_data = load_tags_data(self.tags_filepath)
        self.vectorizer, self.tfidf_matrix = initialize_search(self.movies_data)

        # Erstelle das Layout
        self.create_widgets()

    def create_widgets(self):
        # Eingabefeld für Filmtitel
        self.title_entry = tk.Entry(self.root, width=50)
        self.title_entry.pack()

        # Suchen-Button
        self.search_button = tk.Button(self.root, text="Film suchen", command=self.search_movie)
        self.search_button.pack()

        # Textfeld für die Ergebnisse
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack()

    def search_movie(self):
        # Benutzereingabe holen
        user_input_title = self.title_entry.get()
        movie_id, movie_title = find_movie_by_title(user_input_title, self.movies_data)

        if movie_id:
            recs_general = generate_recommendations(movie_id, self.movies_data, self.ratings_data, self.tags_data,
                                                    self.vectorizer, self.tfidf_matrix)
            recs_tags = refine_recommendations(movie_id, self.movies_data, self.tags_data)

            # Kombiniere die Empfehlungen
            combined_recs = combine_recommendations(recs_general, recs_tags)

            # Ergebnisse im Textfeld anzeigen
            self.result_text.delete(1.0, tk.END)  # Vorherige Ergebnisse löschen
            self.result_text.insert(tk.END, combined_recs.to_string(index=False))
        else:
            messagebox.showinfo("Suche", "Film konnte nicht gefunden werden.")


# Hauptfunktion zum Ausführen der App
def run_app():
    root = tk.Tk()
    MovieRecommenderGUI(root)
    root.mainloop()


if __name__ == '__main__':
    run_app()
