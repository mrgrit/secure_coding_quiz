import sqlite3
from flask import Flask, request

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("payments.db")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS cards (user_id INTEGER, holder TEXT, card_no TEXT, expiry TEXT)"
    )
    conn.commit()
    conn.close()


@app.route("/cards", methods=["POST"])
def save_card():
    conn = sqlite3.connect("payments.db")
    conn.execute(
        "INSERT INTO cards (user_id, holder, card_no, expiry) VALUES (?, ?, ?, ?)",
        (
            request.form["user_id"],
            request.form["holder"],
            request.form["card_no"],
            request.form["expiry"],
        ),
    )
    conn.commit()
    conn.close()
    return "saved", 201
