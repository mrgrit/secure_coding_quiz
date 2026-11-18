import os
import sqlite3
from flask import Flask, request, session, jsonify
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    conn = sqlite3.connect("users.db")
    row = conn.execute(
        "SELECT id, pw_hash FROM users WHERE username = ?", (username,)
    ).fetchone()
    conn.close()
    if row is not None and check_password_hash(row[1], password):
        session["user_id"] = row[0]
        return jsonify(ok=True)
    return jsonify(ok=False), 401
