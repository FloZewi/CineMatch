# CineMatch: Dein persönlicher Filmempfehlungsgenerator

### Projektbeschreibung

CineMatch ist ein personalisiertes Filmempfehlungssystem, das fortschrittliche Techniken aus dem Bereich des maschinellen Lernens und der künstlichen Intelligenz nutzt. Das Ziel von CineMatch ist es, Nutzern Filmempfehlungen zu geben, die auf deren individuellen Sehgewohnheiten basieren. Durch die Analyse des Sehverhaltens und der Präferenzen der Benutzer kann CineMatch Vorhersagen treffen, welche Filme den Benutzern gefallen könnten.


### Datenquelle
Das Empfehlungssystem verwendet das umfangreiche MovieLens 25M Dataset, welches über folgenden Link zugänglich ist: 
https://files.grouplens.org/datasets/movielens/ml-25m.zip


### Technologie

CineMatch wurde in Python entwickelt und verwendet verschiedene Bibliotheken wie Tkinter für die grafische Benutzeroberfläche, Pandas für die Datenmanipulation, Scikit-learn für maschinelles Lernen sowie Algorithmen zur Ähnlichkeitsberechnung.



### Setup und Ausführung
Folge diesen Schritten, um CineMatch zu installieren und auszuführen:


***Klonen des Repositories:***

        git clone https://github.com/FloZewi/CineMatch.git



***Installation der Abhängigkeiten:***

Stelle sicher, dass Python installiert ist und installiere die erforderlichen Python-Pakete:

        pip install pandas scikit-learn



***Daten herunterladen:***

Lade das MovieLens 25M Dataset herunter und entpacke es im Hauptverzeichnis.



**Starten der Anwendung:***

Öffne das Terminal oder die Kommandozeile und führe das Skript gui_interface.py aus:

        python gui_interface.py



***Verwendung der Anwendung:***

Geben Sie den Titel des Films (z.B. Toy Story) in das Eingabefeld ein und klicken Sie auf "Film suchen", um personalisierte Empfehlungen zu erhalten.




### Features

- Filmempfehlungen basierend auf individuellen Präferenzen
- Tag-basierte und kollaborative Filterungsmethoden
- Grafische Benutzeroberfläche für eine einfache Interaktion



### Lizenz

Dieses Projekt ist lizenziert unter der MIT Lizenz - https://opensource.org/licenses/MIT
