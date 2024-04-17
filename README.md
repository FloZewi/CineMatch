# CineMatch: Dein persönlicher Filmempfehlungsgenerator


### Projektbeschreibung

CineMatch ist ein personalisiertes Filmempfehlungssystem, das Techniken aus dem Bereich des maschinellen Lernens und der künstlichen Intelligenz nutzt. Das Ziel von CineMatch ist es, Nutzern Filmempfehlungen zu geben, die auf deren individuellen Sehgewohnheiten basieren. Durch die Analyse des Sehverhaltens und der Präferenzen der Benutzer kann CineMatch Vorhersagen treffen, welche Filme den Benutzern gefallen könnten.



### Datenquelle
Das Empfehlungssystem verwendet das umfangreiche MovieLens 25M Dataset, welches über folgenden Link zugänglich ist: 
https://files.grouplens.org/datasets/movielens/ml-25m.zip



### Technologie

CineMatch wurde in Python entwickelt und verwendet verschiedene Bibliotheken wie PyQt5 für die grafische Benutzeroberfläche, Pandas für die Datenmanipulation, Scikit-learn für maschinelles Lernen sowie Algorithmen zur Ähnlichkeitsberechnung.




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





### Technische Details

Hier eine Übersicht über die Funktionen der einzelnen Skripte in diesem Projekt:
        
- In **'data_exploration.py'** werden Datananlyse- und Visualisierungsfunktionen zur Untersuchung des Datensatzes bereitgestellt. Es ermöglicht das Anzeigen von Datensatzdimensionen, statistischen Zusammenfassungen und das Erkennen von fehlenden Daten. Darüber hinaus unterstützt es die Visualisierung durch Histogramme, Boxplots und Korrelations-Heatmaps, um ein tiefgehendes Verständnis für die Verteilung und Beziehung der Daten zu erhalten. Diese Analyse hilft, wichtige Einsichten zu gewinnen, bevor komplexe Datenverarbeitungs- oder maschinelle Lernverfahren angewendet werden. 
        
- In **'data_preparation.py'** wird eine Funktion verwendet, um Filmdaten aus einer CSV-Datei zu laden und die Filmtitel zu bereinigen. Die bereinigten Titel werden als neue Spalte dem DataFrame hinzugefügt.

- In **'data_utils.py'** sind mehrere Hilfsfunktionen definiert, die beim Laden und Vorverarbeiten von Daten genutzt werden.

- **'search.py'** implementiert die Suchfunktionalität für das Filmempfehlungssystem mit TF-IDF und Konsinusähnlichkeit, um relevante Filme basierend auf Textsuche zu finden.

- Das Modul **'recommendation.py'** implementiert die Kernlogik des Empfehlungssystems von CineMatch und umfasst verschiedene Funktionen zur Datenmanipulation und Ähnlichkeitsberechnung.

- Die **'main.py'** des CineMatch-Projekts orchestriert den gesamten Prozess der Datenverarbeitung und Generierung von Filmempfehlungen. Hier werden zunächst die notwendigen Daten geladen, darunter Filminformationen, Bewertungen und Tags. Anschließend wird die Suchfunktionalität initialisiert, um es Benutzern zu ermöglichen, nach Filmtiteln zu suchen. Nachdem ein Benutzer einen Filmtitel eingegeben hat, werden passende Filme gesucht und darauf basierend Empfehlungen generiert, die sowohl allgemeine als auch tag-basierte Empfehlungsmehtoden kombinieren. Diese Empfehlungen werden dann im Terminal ausgegeben. Die 'main.py' ermöglicht so eine direkte Interaktion mit dem Empfehlungssystem über die Konsole.

- Das Hauptprogramm **'gui_interface.py'** implementiert eine grafische Benutzeroberfläche (GUI) für das CineMatch Filmempfehlungssystem unter Verwendung von PyQt5. Diese Benutzeroberfläche ermöglicht es Benutzern, Filmtitel einzugeben und darauf basierend personalisierte Empfehlungen zu erhalten. Diese Implementierung bietet eine benutzerfreundliche Möglichkeit, Filmempfehlungen interaktiv zu erhalten um die Ergebnisse übersichtilich in einer Tabelle dargestellt zu bekommen.  




### Lizenz

Dieses Projekt ist lizenziert unter der MIT Lizenz - https://opensource.org/licenses/MIT
