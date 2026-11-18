import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_PATH = "shop.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/orders")
def list_orders():
    customer = request.args.get("customer", "")
    status = request.args.get("status", "paid")
    conn = get_db()
    query = (
        "SELECT id, item, price FROM orders WHERE customer = '"
        + customer
        + "' AND status = '"
        + status
        + "'"
    )
    rows = conn.execute(query).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


if __name__ == "__main__":
    app.run()
