import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget,
                             QMessageBox, QTableWidget, QTableWidgetItem)
from data_preparation import prepare_movies_data
from search import initialize_search, find_movie_by_title
from recommendation import generate_recommendations, refine_recommendations, combine_recommendations
from data_utils import load_data, load_tags_data


class MovieRecommenderGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CineMatch: Dein persönlicher Filmempfehlungsgenerator")

        # Initialisierung der Instanz attribute
        self.movie_filepath = 'movies.csv'
        self.ratings_filepath = 'ratings.csv'
        self.tags_filepath = 'tags.csv'
        self.movies_data = prepare_movies_data(self.movie_filepath)
        self.ratings_data = load_data(self.ratings_filepath)
        self.tags_data = load_tags_data(self.tags_filepath)
        self.vectorizer, self.tfidf_matrix = initialize_search(self.movies_data)

        self.init_ui()

    def init_ui(self):
        # Widgets erstellen
        self.title_entry = QLineEdit(self)
        self.search_button = QPushButton('Film suchen', self)
        self.results_table = QTableWidget(self)  # Tabelle für Ergebnisse verwenden

        # Tabelle einrichten
        self.results_table.setColumnCount(3)  # Anzahl der Spalten anpassen
        self.results_table.setHorizontalHeaderLabels(['Titel', 'Movie ID', 'Durchschnittsbewertung'])  # Spalten-
        # überschriften setzen

        # Layout festlegen
        layout = QVBoxLayout()
        layout.addWidget(self.title_entry)
        layout.addWidget(self.search_button)
        layout.addWidget(self.results_table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Verbinden des Suchbuttons mit der Funktion search_movie
        self.search_button.clicked.connect(self.search_movie)

    def search_movie(self):
        user_input_title = self.title_entry.text()
        movie_id, movie_title = find_movie_by_title(user_input_title, self.movies_data)

        if movie_id:
            recs_general = generate_recommendations(movie_id, self.movies_data, self.ratings_data, self.tags_data,
                                                    self.vectorizer, self.tfidf_matrix)
            recs_tags = refine_recommendations(movie_id, self.movies_data, self.tags_data)

            # Empfehlungen kombinieren
            combined_recs = combine_recommendations(recs_general, recs_tags)

            # Empfehlungen in der Tabelle anzeigen
            if not combined_recs.empty:
                self.display_results(combined_recs)
            else:
                QMessageBox.information(self, "Keine Empfehlungen", "Es wurden keine Empfehlungen gefunden.")
        else:
            QMessageBox.information(self, "Suche", "Film konnte nicht gefunden werden.")

    def display_results(self, combined_recs):
        # Bestehende Ergebnisse löschen
        self.results_table.setRowCount(0)
        self.results_table.setColumnCount(len(combined_recs.columns))
        self.results_table.setHorizontalHeaderLabels(combined_recs.columns.tolist())

        # Daten in die Tabelle eintragen
        for index, row in combined_recs.iterrows():
            row_num = self.results_table.rowCount()
            self.results_table.insertRow(row_num)
            for col_num, item in enumerate(row):
                self.results_table.setItem(row_num, col_num, QTableWidgetItem(str(item)))

        self.results_table.resizeColumnsToContents()  # Spaltenbreite an den Inhalt anpassen


def run_app():
    app = QApplication(sys.argv)
    main_win = MovieRecommenderGUI()
    main_win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_app()
