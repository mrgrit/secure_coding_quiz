import logging
import sqlite3
from flask import Flask, request
from werkzeug.security import generate_password_hash

app = Flask(__name__)
logging.basicConfig(filename="app.log", level=logging.INFO)


@app.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    logging.info("signup request user=%s password=%s", username, password)
    conn = sqlite3.connect("users.db")
    conn.execute(
        "INSERT INTO users (username, pw_hash) VALUES (?, ?)",
        (username, generate_password_hash(password)),
    )
    conn.commit()
    conn.close()
    return "created", 201
