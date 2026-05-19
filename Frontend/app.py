from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Demo-Daten
# Werden später durch OpenCV ersetzt

game_data = {
    "game_mode": "501 Double Out",
    "current_player": "Justin",
    "last_hit": "TRIPLE 20",
    "points": 60,
    "round": 12,
    "legs": "1 : 0",
    "players": [
        {
            "name": "Justin",
            "score": 241,
            "average": 58.2,
            "checkout": "T20 D20",
            "darts": ["T20", "T19", "D10"]
        },
        {
            "name": "Alex",
            "score": 301,
            "average": 52.4,
            "checkout": "-",
            "darts": ["BULL", "5", "-"]
        }
    ],
    "history": [
        "Justin → Triple 20 (+60)",
        "Justin → Triple 19 (+57)",
        "Alex → Bullseye (+50)",
        "Alex → Single 5 (+5)"
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/game')
def game():
    return jsonify(game_data)

if __name__ == '__main__':
    app.run(debug=True)