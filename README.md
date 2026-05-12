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

---

## 👥 Team
*Justin Marchi, Luca Ratz, Paul Peter, Christopher Enk*
