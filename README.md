Projektbeschreibung:
Entwicklung eines kamerabasierten Hardware-Software-Systems zur automatischen Punktzählung beim Steeldart. Das System nutzt drei Kameraperspektiven zur Triangulation der Pfeilposition sowie einen piezoelektrischen Vibrationssensor zur zuverlässigen Einschlagserkennung. Die Verarbeitung erfolgt über einen Laptop mittels Computer Vision (OpenCV).
BENÖTIGTE KOMPONENTEN (MATERIALSCHEIN)
1. ELEKTRONIK UND SENSORIK
* 3x USB-Kameramodule (OV2710): Full-HD Auflösung, 30-60 FPS, Weitwinkelobjektiv. Notwendig für die optische Erfassung der Pfeile aus drei Winkeln zur Vermeidung von Verdeckungen.
* 1x Mikrocontroller (Arduino Nano oder ESP32): Dient als Interface zwischen der analogen Sensorik (Piezo) und dem Laptop.
* 2x Piezo-Vibrationssensoren (20-27mm): Zur Detektion des physikalischen Einschlags am Board. Ermöglicht einen effizienten Software-Trigger und schont die CPU-Last des Laptops.
* 1x Aktiver USB 3.0 Hub (mit Netzteil): Zwingend erforderlich, um die hohe Datenrate von drei parallelen Videostreams stabil zu verarbeiten und die USB-Ports des Laptops zu entlasten.
* 3x USB 2.0/3.0 Verlängerungskabel (3m): Zur Verbindung der Kameras am Montage-Ring mit dem zentralen Steuerungs-Laptop.
2. MECHANIK UND FERTIGUNG (3D-DRUCK)
* 1.5 kg Filament (PLA Pro oder PETG, Schwarz-Matt): Material für das modulare Halterungssystem (Ring-Segmente und Kamera-Arme). Mattes Schwarz minimiert Lichtreflexionen, die die Bildverarbeitung stören könnten.
* Gewindeeinsätze (Heat-Inserts):
* 18x M3 Heat-Inserts (für die Ring-Verbindungen)
* 12x M4 Heat-Inserts (für die Montage der Kamera-Arme)
* Zylinderkopfschrauben (DIN 912):
* 18x M3x8mm (Verbindung der Ringelemente)
* 6x M4x16mm (Montage Ring an Standfüße)
* 6x M4x12mm (Montage Gehäuse an Arme)
* 15x M2x6mm (Befestigung der Kamera-Platinen und Gehäusedeckel)
3. VERBRAUCHSMATERIAL UND KLEINTEILE
* Widerstand (1M Ohm): Zur Pegelanpassung des Piezo-Signals am Arduino.
* Kabelmaterial: Jumper-Kabel und Schaltdraht für die interne Verkabelung von LEDs und Sensoren.
* Montagematerial: Doppelseitiges Klebeband zur Fixierung des Piezo-Sensors auf der Board-Rückseite.
VORHANDENE RESSOURCEN (KEINE ANSCHAFFUNG NÖTIG)
* Recheneinheit: Laptop (Intel Core i5/i7) zur Bildanalyse und Darstellung der Benutzeroberfläche.
* Dart-Equipment: Bristle Dartboard und Surround.
* Beleuchtung: LED-Strip (12V) für schattenfreie Ausleuchtung des Spielfelds.
* Fertigungskapazität: Zugriff auf 3D-Drucker im Studentslab.
TECHNISCHE HIGHLIGHTS DES ENTWURFS
* Triangulation: Höchste Präzision durch 3-Kamera-Setup.
* Sensor-Fusion: Kombination aus optischen Daten und Vibrations-Trigger reduziert Fehlwürfe (z.B. durch Personen im Bild).
* Wartbarkeit: Einsatz von Heat-Inserts ermöglicht dauerhafte Stabilität und einfache Demontage im Vergleich zu direkten Verschraubungen in Kunststoff.
