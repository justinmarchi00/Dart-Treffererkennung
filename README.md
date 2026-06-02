# 🎯 Automatisiertes Dart-Scoring-System

## 📌 Projektbeschreibung
Dieses Projekt beschäftigt sich mit der Entwicklung eines **kamerabasierten Hardware-Software-Systems**, das automatisch die Punkte beim Steeldart zählt.

Das System nutzt:
- **drei Kameras**, um die Position der Dartpfeile zu bestimmen (Triangulation)
- einen **piezoelektrischen Vibrationssensor**, um den Einschlag eines Pfeils zu erkennen
- **Computer Vision mit OpenCV**, um die Bilddaten auszuwerten

Die gesamte Verarbeitung erfolgt auf einem Laptop, der die Daten von Kameras und Sensoren kombiniert.

---

## ⚙️ Funktionsweise
1. Ein Dartpfeil trifft das Board  
2. Der **Piezo-Sensor** erkennt die Vibration → Signal wird ausgelöst  
3. Die **Kameras nehmen gleichzeitig Bilder auf**  
4. Die Software berechnet mithilfe der drei Perspektiven die genaue Position des Pfeils  
5. Die entsprechende Punktzahl wird automatisch bestimmt und angezeigt  

---

## 🧰 Benötigte Komponenten (Materialschein)

### 🔌 Elektronik und Sensorik
- **3x USB-Kameramodule (OV2710)**  
  Full-HD, 30–60 FPS, Weitwinkel → zur Erfassung aus mehreren Winkeln  

- **1x Mikrocontroller (Arduino Nano oder ESP32)**  
  Verbindung zwischen Sensor und Laptop  

- **2x Piezo-Vibrationssensoren (20–27 mm)**  
  Erkennt den Einschlag des Pfeils  

- **1x Aktiver USB 3.0 Hub (mit Netzteil)**  
  Für stabile Datenübertragung von 3 Kameras  

- **3x USB-Verlängerungskabel (ca. 3 m)**  
  Für flexible Platzierung der Kameras  

---

### 🛠️ Mechanik und Fertigung (3D-Druck)
- **1,5 kg Filament (PLA Pro oder PETG, schwarz-matt)**  
  Für Halterungen und Kamerarig  

#### Gewindeeinsätze (Heat-Inserts)
- 18x M3  
- 12x M4  

#### Schrauben (DIN 912)
- 18x M3x8 mm  
- 6x M4x16 mm  
- 6x M4x12 mm  
- 15x M2x6 mm  

---

### 🔧 Verbrauchsmaterialien
- **1M Ohm Widerstand** → Anpassung des Sensorsignals  
- **Kabel (Jumper, Schaltdraht)** → interne Verbindungen  
- **Doppelseitiges Klebeband** → Befestigung des Sensors  

---

## 💻 Vorhandene Ressourcen
Diese Komponenten müssen **nicht angeschafft werden**:
- Laptop (Intel i5/i7)
- Dartboard + Surround
- LED-Beleuchtung (12V)
- 3D-Drucker im StudentsLab  

---

## 🚀 Technische Highlights

### 📐 Triangulation
Durch drei Kameras wird die Position des Pfeils sehr genau bestimmt.

### 🔄 Sensor-Fusion
Kombination aus:
- Bildverarbeitung (Kameras)
- physikalischem Signal (Sensor)

→ reduziert Fehler deutlich

### 🔩 Wartbarkeit
Durch **Heat-Inserts**:
- stabilere Konstruktion  
- einfache Demontage möglich  
- langlebiger als direkte Schrauben im Kunststoff  

---

## 📊 Kostenübersicht
Die Kosten für neue Komponenten liegen bei etwa:

**120 € – 150 €**

→ sehr effizient für ein Projekt mit mehreren Personen

---

## 🧪 Geplante Umsetzung
- Aufbau eines Kamerasystems um das Dartboard  
- Verbindung aller Komponenten mit dem Laptop  
- Entwicklung der Software mit **OpenCV**  
- Testen und Optimieren der Treffererkennung  

---

## 🎯 Ziel des Projekts
Ein funktionierendes System, das:
- automatisch Punkte erkennt  
- zuverlässig arbeitet  
- einfach zu bedienen ist  

---

## 📸 Beispielbild

<img width="1588" height="2117" alt="Image" src="https://github.com/user-attachments/assets/1ea0431b-4e36-47dc-8f1a-193951b64fb5" />

*Quelle: https://i.etsystatic.com/58075119/r/il/a46dd5/7300756379/il_1588xN.7300756379_7i1j.jpg*
---


## Bilder vom 3D-Druck

<img width="768" height="1024" alt="323033FD-1292-4B2C-9FC0-E6FA3B946680_1_105_c" src="https://github.com/user-attachments/assets/edfa5c91-8a8e-4359-9e19-bc8c76d06821" /><img width="768" height="1024" alt="6D8AF519-F548-4133-8493-95B29EE4C09D_1_105_c" src="https://github.com/user-attachments/assets/5cb19155-b29e-4578-a432-52a6d8358f59" /><img width="768" height="1024" alt="6D8AF519-F548-4133-8493-95B29EE4C09D_1_105_c" src="https://github.com/user-attachments/assets/a14b1873-5cc8-498c-a897-1a50ad1a51cf" />
<img width="768" height="1024" alt="DD6F4A32-9B25-4479-8145-BB8CA59A4E09_1_105_c" src="https://github.com/user-attachments/assets/0999a07a-1a68-4ebc-a6ea-73177fc49e76" />
<img width="768" height="1024" alt="DAD65EB5-A7B7-4D04-B31F-C83C963C70C9_1_105_c" src="https://github.com/user-attachments/assets/3f414325-9621-4be7-8108-22cc8afc72c7" />


## Bilder Frontend
<img width="1280" height="832" alt="PHOTO-2026-06-02-15-19-32" src="https://github.com/user-attachments/assets/478b675e-a360-45ca-a12c-630fb947333f" />
# Kosten Kalkulation

| Pos. | Bezeichnung | Beschreibung | Link | Anzahl | Preis | Gesamt |
|------|-------------|--------------|------|--------|-------|---------|
| 1 | Dartscheibe | Dartscheibe | besitzen wir schon | 1 | - € | - € |
| 2 | Darts Camera and LED Ring mount | Konstruktion Kameras | [Printables](https://www.printables.com/model/875543-darts-camera-and-led-ring-mount-by-3dengelen#hardware-required-) | 1 | - € | - € |
| 3 | OV9732 Kameramodul 3er Set | Kamera | [Amazon](https://www.amazon.de/) | 3 | 9,92 € | 29,76 € |
| 4 | Aufprallsensor | Aufprallsensor | [Reichelt](https://www.reichelt.de/) | 2 | 2,70 € | 5,40 € |
| 5 | Arduino - Piezo Vibrationssensor | Arduino | besitzen wir schon | 1 | - € | - € |
| 6 | USB 3.0 Hub | USB 3.0 Hub | [Amazon](https://www.amazon.de/) | 1 | 13,99 € | 13,99 € |
| 7 | Verlängerungskabel USB | Verlängerungskabel USB | [Reichelt](https://www.reichelt.de/) | 1 | 19,99 € | 19,99 € |
| 8 | M3, M4 Gewindeeinsätze | M3 Gewindeeinsätze | [Amazon](https://www.amazon.de/) | 1 | 19,99 € | 19,99 € |
| 9 | M3*8mm Flachkopfschrauben | M3 Schrauben | [Amazon](https://www.amazon.de/) | 1 | 5,99 € | 5,99 € |
| 10 | M4x16 mm Flachkopfschrauben | M4 Schrauben | [Amazon](https://www.amazon.de/) | 1 | 6,99 € | 6,99 € |
| 11 | M4x12 mm Flachkopfschrauben | M4 Schrauben | [Amazon](https://www.amazon.de/) | 1 | 6,99 € | 6,99 € |
| 12 | M2x6 Schrauben, Zylinderkopfschrauben | M2 Schrauben | [Amazon](https://www.amazon.de/) | 1 | 4,99 € | 4,99 € |
| 13 | Widerstände Arduino | Widerstände Arduino | besitzen wir schon | 1 | - € | - € |
| 14 | Kabelmaterial | Kabelmaterial | besitzen wir schon | 1 | - € | - € |
| 15 | Filament Schwarz PETG | Filament | Herr Dirks bestellt Filament | 2 | 25,00 € | 50,00 € |

---

## Gesamt

**164,09 €**


## 👥 Team
*Justin Marchi, Luca Ratz, Paul Peter, Christopher Enk*
