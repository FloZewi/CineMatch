import pandas as pd
import re


def load_data(filepath):
    """Lädt Daten aus einer CSV-Datei und gibt ein DataFrame zurück."""
    try:
        data = pd.read_csv(filepath)
        print(f"Daten erfolgreich aus {filepath} geladen.")
        return data
    except FileNotFoundError:
        print(f"Fehler: Datei {filepath} nicht gefunden.")
        return None


def clean_title(title):
    """Bereinigt Filmtitel von Sonderzeichen und entfernt das Jahr."""
    # Enfernt das Jahr am Ende des Titels
    title_without_year = re.sub(r' \(\d{4}\)$', '', title)
    # Bereinigt den Titel von Sonderzeichen
    cleaned_title = re.sub(pattern='[^a-zA-Z0-9 ]', repl='', string=title_without_year)
    return cleaned_title
