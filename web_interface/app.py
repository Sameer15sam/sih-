from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Database file
DB_FILE = "database/track_fittings.db"

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Fetch all track fittings
@app.route("/fittings", methods=["GET"])
def fetch_fittings():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM track_fittings")
    fittings = cursor.fetchall()
    conn.close()
    return jsonify(fittings)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)