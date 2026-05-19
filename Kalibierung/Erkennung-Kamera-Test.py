import cv2
import numpy as np

# Schwarzes Bild erzeugen
img = np.zeros((500, 500, 3), dtype=np.uint8)

# Kreis zeichnen
cv2.circle(img, (250, 250), 100, (0, 255, 330), 5)

# Text schreiben
cv2.putText(
    img,
    "OpenCV funktioniert!",
    (70, 450),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 244, 255),
    2
)

# Fenster anzeigen
cv2.imshow("Test", img)

# Warten bis Taste gedrückt wird
cv2.waitKey(0)

# Fenster schließen
cv2.destroyAllWindows()