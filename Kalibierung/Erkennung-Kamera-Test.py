import cv2

# Liste aller Kamera-Indizes, die geöffnet werden sollen
camera_indices = [0, 1, 2]
cameras = []

# Kameras initialisieren und prüfen, welche verfügbar sind
for index in camera_indices:
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        cameras.append((index, cap))
        print(f"Kamera {index} erfolgreich gestartet.")
    else:
        cap.release()
        print(f"Kamera {index} ist nicht verfügbar.")

# Falls überhaupt keine Kamera gefunden wurde, das Skript beenden
if not cameras:
    print("Error: Keine funktionierenden Kameras gefunden.")
    exit()

while True:
    for index, cap in cameras:
        ret, frame = cap.read()
        
        if ret:
            # Zeigt jede Kamera in einem eigenen Fenster an
            cv2.imshow(f'Kamera Feed {index}', frame)
        else:
            print(f"Fehler beim Lesen von Kamera {index}.")

    # Drücken Sie 'q', um alle Feeds zu schließen
    if cv2.waitKey(1) == ord('q'):
        break

# Alle aktiven Kamera-Ressourcen freigeben
for index, cap in cameras:
    cap.release()

cv2.destroyAllWindows()
