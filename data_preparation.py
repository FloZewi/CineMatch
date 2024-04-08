import pandas as pd
import re


# Funktion zum Laden von Daten aus einer CSV-Datei
def load_data(filepath):
    """Lädt Daten aus einer CSV-Datei und gibt ein DataFrame zurück."""
    print(f"Lade Daten aus {filepath}...")
    data = pd.read_csv(filepath)
    print("Erste 5 Zeilen der geladenen Daten:")
    print(data.head())
    return data


# Funktion zur Bereinigung von Filmtiteln, entfernt alle Nicht-Alphanumerischen Zeichen
def clean_title(title):
    # Vor der Bereinigung den Originaltitel anzeigen
    print(f"Originaltitel: {title}")
    cleaned_title = re.sub(pattern='[^a-zA-Z0-9 ]', repl="", string=title)
    # Nach der Bereinigung den bereinigten Titel anzeigen
    print(f"Bereinigter Titel: {cleaned_title}")
    return cleaned_title


# Hauptfunktion zur Vorbereitung der Filmdaten:
# Lädt die Daten, bereinigt die Titel und fügt diese als neue Spalte hinzu
def prepare_movies_data():
    movies_data = load_data("movies.csv")
    # Anwenden der clean_title-Funktion auf jede Zeile im Titel
    movies_data['clean_title'] = movies_data['title'].apply(clean_title)
    print("\nDaten nach der Bereinigung der Titel:")
    print(movies_data.head())  # Zeigt die ersten fünf Zeilen des aktualisierten DataFrame
    return movies_data


# Hauptfunktion aufrufen
prepared_data = prepare_movies_data()

# Ausgabe der Informationen zum DataFrame
print("\nInformationen zum vorbereiteten DataFrame:")
print(prepared_data.info())

# Abschließende Zeile, um zu signalisieren, dass das Script vollständig ausgeführt wurde
print("\nVorbereitung der Filmdaten abgeschlossen.")
