import tkinter as tk
from tkinter import ttk, messagebox     # ttk für verbesserte Widgets
import platform
from data_preparation import prepare_movies_data
from search import initialize_search, find_movie_by_title
from recommendation import generate_recommendations, refine_recommendations, combine_recommendations
from data_utils import load_data, load_tags_data


# Haupt-GUI-Klasse
class MovieRecommenderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CineMatch: Dein persönlicher Filmempfehlungsgenerator")

        # Initialisierung aller Instanz attribute
        self.movie_filepath = 'movies.csv'
        self.ratings_filepath = 'ratings.csv'
        self.tags_filepath = 'tags.csv'
        self.movies_data = prepare_movies_data(self.movie_filepath)
        self.ratings_data = load_data(self.ratings_filepath)
        self.tags_data = load_tags_data(self.tags_filepath)
        self.vectorizer, self.tfidf_matrix = initialize_search(self.movies_data)

        self.title_entry = tk.Entry(self.root, width=50)
        self.search_button = ttk.Button(self.root, text="Film suchen", command=self.search_movie)
        self.result_text = tk.Text(self.root, height=10, width=50)

        self.padding = (2, 2)       # Standard-Padding für nicht macOS

        # System-spezifische Optionen
        self.set_system_specific_options()

        # Erstelle das Layout
        self.create_widgets()

    def set_system_specific_options(self):
        # Anpassungen für macOS
        if platform.system() == "Darwin":
            self.root.tk.call('tk', 'scaling', 1.5)
            style = ttk.Style()
            style.theme_use('aqua')
            style.configure('TButton', font=('Helvetica', 12), padding=6)
            style.configure('TEntry', font=('Helvetica', 12), padding=6)
            style.configure('TText', font=('Helvetica', 12), padding=6)
            self.padding = (10, 5)      # Anpassen des Paddings für macOS
        else:
            self.padding = (2, 2)

    def create_widgets(self):
        # Widgets werden entsprechend der zuvor gesetzten Systemeinstellungen erstellt
        # Eingabefeld für Filmtitel
        self.title_entry.pack(padx=self.padding[0], pady=self.padding[1])
        # Suchen-Button
        self.search_button.pack(pady=self.padding[1])
        # Textfeld für die Ergebnisse
        self.result_text.pack(padx=self.padding[0], pady=self.padding[1])

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

    if platform.system() == "Darwin":
        root.tk.call('tk', 'scaling', 1.5)  # Verbessere Skalierung auf hochauflösenden Bildschirmen

    MovieRecommenderGUI(root)
    root.mainloop()


if __name__ == '__main__':
    run_app()
