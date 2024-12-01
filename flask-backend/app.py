from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, content TEXT)''')
    cursor.execute("INSERT OR IGNORE INTO messages (id, content) VALUES (1, 'Hello, World!')")
    conn.commit()
    conn.close()

@app.route('/api/hello', methods=['GET'])
def hello():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM messages WHERE id=1")
    message = cursor.fetchone()[0]
    conn.close()
    return jsonify(message=message)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
