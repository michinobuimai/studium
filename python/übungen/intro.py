# ==============================================================================
# SPICKZETTEL: PYTHON DATENTYPEN, VARIABLEN, LISTEN & KONTROLLSTRUKTUREN
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. BASIS-DATENTYPEN testtest
# ------------------------------------------------------------------------------
# Integer (int)   : Ganzzahlen (z. B. 5, -3)
# Float (float)   : Gleitkommazahlen. Wichtig: Divisionen (/) liefern IMMER ein Float!
# Boolean (bool)  : True oder False (Achtung: Case-Sensitive! 'true' ist ungültig)
# String (str)    : Zeichenketten in Einfach- oder Doppelanführungszeichen

# Tipp: Einzelne Zeilen/Snippets im Editor testen mit: [Markierung] + Shift + Enter


# ------------------------------------------------------------------------------
# 2. TYP-KONVERTIERUNG (Type Casting)
# ------------------------------------------------------------------------------
# Syntax: [Datentyp]([Wert])

# Gibt 3 zurück (Nachkommastellen werden abgeschnitten / floored)
print(int(3.14159))

# Gibt 3.0 zurück
print(float(3))

# Boolesche Konvertierung: 0, "" (leerer String) und leere Listen sind False. Alles andere ist True!
print(bool(0))  # Gibt False zurück
print(bool(5))  # Gibt True zurück

# Fortgeschritten: Strings mit Angabe der Basis konvertieren (z. B. Hexadezimal)
x = int("abc", base=16)
print(f"{x}")  # Gibt 2748 zurück


# ------------------------------------------------------------------------------
# 3. VARIABLEN-NAMENSREGELN
# ------------------------------------------------------------------------------
# - Erlaubte Zeichen: [a-z], [A-Z], [0-9], [_]
# - Darf NICHT mit einer Zahl beginnen! (z. B. '5x' ist ungültig, '_5x' ist gültig)
# - Variablen sind CASE-SENSITIVE (x ist nicht gleich X; alter != Alter != ALTER)

_5x = "Hello,"
y = "World!"
print(_5x + " " + y)  # Gibt "Hello, World!" zurück


# ------------------------------------------------------------------------------
# 4. STRINGS & FORMATIERUNG
# ------------------------------------------------------------------------------
# Escaping: Anführungszeichen im String per Backslash (\) maskieren oder die jeweils 
# anderen Anführungszeichen außen nutzen:
# "He said, \"Hello!\""  ODER  'He said, "Hello!"'

# F-Strings (Formatierte Strings):
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Benutzereingabe: input() liefert IMMER einen String und muss ggf. gecastet werden!
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))  # Direkt zu int konvertiert


# ------------------------------------------------------------------------------
# 5. LISTEN & SLICING
# ------------------------------------------------------------------------------
# Syntax: liste[start_index : end_index : schrittweite]
# Wichtig: Der end_index ist EXKLUSIVE (wird nicht mehr mitgezählt)!

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(liste)

# Schrittweite negativ -> Invertiert die gesamte Liste
liste2 = liste[::-1]
print(liste2)  # [15, 14, ..., 1]

# Start bei Index 1 (Wert 2) bis Index 10 (exklusive), in 2er-Schritten
liste3 = liste[1:10:2]
print(liste3)  # Gibt [2, 4, 6, 8, 10] zurück

# liste.pop([index]) -> Entfernt das Element am angegebenen Index und gibt es zurück
liste3.pop(3)  # Entfernt das Element an Index 3 (Wert 8)
print(liste3)  # Gibt [2, 4, 6, 10] zurück


# ------------------------------------------------------------------------------
# 6. VERGLEICHE & KONDITIONEN (if, elif, else)
# ------------------------------------------------------------------------------
# Verkettete Vergleiche: Python erlaubt die mathematische Schreibweise: start < x < ende

x = 2
boolean = 0 < x < 2
print(f"{boolean}")  # Gibt False zurück

# Verzweigungen mit if, elif und else:
x = 2
if 3 < x < 5:
    print("True")
elif x == 2:
    print("is 2")
else:
    print("False")


# ------------------------------------------------------------------------------
# 7. SCHLEIFEN (Loops)
# ------------------------------------------------------------------------------
# While-Schleife (Bedingungsgesteuert)
i = 0
while i < 10:
    print(i)  # Gibt 0 bis 9 aus
    i = i + 1  # Alternativ: i += 1

# For-Schleife (Zählergesteuert mit range)
# range(10) erzeugt Zahlen von 0 bis 9 (die 10 ist exklusive!)
for i in range(10):
    print(i)  # Gibt 0 bis 9 aus


# ------------------------------------------------------------------------------
# 8. WICHTIGE LISTEN-METHODEN (Neu hinzugefügt)
# ------------------------------------------------------------------------------
meine_liste = [1, 2, 3]

# .append(wert) -> Fügt ein einzelnes Element am Ende hinzu (als EIN Element)
meine_liste.append(4)          # Liste ist jetzt: [1, 2, 3, 4]
meine_liste.append([5, 6])     # Achtung! Fügt die Liste als Unterliste hinzu: [1, 2, 3, 4, [5, 6]]

# .extend(iterable) -> Schmilzt die Elemente einer anderen Liste am Ende an (Flach)
wichtige_zahlen = [1, 2, 3, 4]
wichtige_zahlen.extend([5, 6]) # Liste ist jetzt: [1, 2, 3, 4, 5, 6]

# .insert(index, wert) -> Fügt ein Element an einer gezielten Position ein
wichtige_zahlen.insert(0, 99)  # Schiebt die 99 ganz nach vorne: [99, 1, 2, 3, 4, 5, 6]

# .remove(wert) -> Sucht nach dem WERT (nicht Index!) und löscht das erste Vorkommen
wichtige_zahlen.remove(99)     # Entfernt die 99 wieder aus der Liste


# ------------------------------------------------------------------------------
# 9. FUNKTIONEN (def)
# ------------------------------------------------------------------------------
# Eine Funktion bündelt Code-Blöcke und kann optionale Parameter sowie Rückgabewerte haben.

# Definition einer einfachen Funktion
def gruesse_user(username):
    print(f"Hallo {username}!")

# Aufruf der Funktion
gruesse_user("Lukas")

# Funktion mit Rückgabewert (return) und Standard-Parameter (Default-Value)
def quadrat_berechnen(zahl=2):
    ergebnis = zahl * zahl
    return ergebnis  # Schickt den Wert zurück an den Aufrufer

# Aufrufe testen:
ergebnis1 = quadrat_berechnen(5)  # Gibt 25 zurück
ergebnis2 = quadrat_berechnen()   # Nutzt den Standardwert (2) und gibt 4 zurück





### paketimport
# bsp. import math
# >> math.sin(math.pi * 0.5) # Gibt 1.0 zurück


### Dateioperationen
# Mit open() kann man Dateien öffnen und lesen oder schreiben.
# Syntax: open(dateiname, modus)
# Modi: 'r' = read, 'w' = write (überschreibt), 'a' = append (hängt an), 'b' = binary (für Binärdateien),
#       'x' = create (erstellt neue Datei, Fehler wenn existiert),       't' = text (Standardmodus)
#       '+' = read & write (kombiniert), 'absolute' = absolute path, 'relative' = relative path

# Beispiel: Lesen einer Textdatei
# with open("beispiel.txt", "r") as datei:
#     inhalt = datei.read()
#     print(inhalt)


