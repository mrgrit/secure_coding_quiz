import sqlite3
import traceback
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/report")
def report():
    try:
        year = int(request.args["year"])
        conn = sqlite3.connect("/srv/app/data/sales.db")
        rows = conn.execute(
            "SELECT month, total FROM sales WHERE year = ?", (year,)
        ).fetchall()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify(error=str(e), trace=traceback.format_exc()), 500
