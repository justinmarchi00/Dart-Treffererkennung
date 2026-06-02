from flask import Flask, jsonify
from flask_cors import CORS

import serial
import serial.tools.list_ports

import threading
import time

app = Flask(__name__)
CORS(app)

# AUTOMATISCHEN ARDUINO PORT FINDEN

arduino_port = None

ports = serial.tools.list_ports.comports()

for port in ports:

    print("Gefundener Port:", port.device)

    if "usbmodem" in port.device or "usbserial" in port.device:

        arduino_port = port.device
        break

if not arduino_port:

    raise Exception("Kein Arduino gefunden!")

print("Arduino verbunden auf:", arduino_port)

# ARDUINO VERBINDUNG

arduino = serial.Serial(arduino_port, 9600)

time.sleep(2)

# STATUS

current_status = "Warte auf Sensor..."

# SERIELLE DATEN LESEN

def read_serial():

    global current_status

    while True:

        try:

            line = arduino.readline().decode().strip()

            if not line:
                continue

            print("Arduino:", line)

            # STATUS ÄNDERN

            if line == "SWITCH_ON":

                current_status = "Sensor erkannt"

            elif line == "SWITCH_OFF":

                current_status = "Sensor bereit"

            elif line == "DART_HIT":

                current_status = "Dart erkannt"

            else:

                current_status = line

        except Exception as e:

            print("Fehler:", e)

# THREAD STARTEN

thread = threading.Thread(target=read_serial)

thread.daemon = True

thread.start()

# API

@app.route('/status')

def status():

    return jsonify({

        'message': current_status

    })

# SERVER STARTEN

app.run(
    host='0.0.0.0',
    port=5050
)