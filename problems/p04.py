import os
from flask import Flask, request

app = Flask(__name__)
UPLOAD_DIR = "/var/www/static/uploads"


@app.route("/profile/photo", methods=["POST"])
def upload_photo():
    f = request.files.get("photo")
    if f is None:
        return "no file", 400
    save_path = os.path.join(UPLOAD_DIR, f.filename)
    f.save(save_path)
    return "uploaded: /static/uploads/" + f.filename, 201


@app.route("/profile/photo/list")
def list_photos():
    names = sorted(os.listdir(UPLOAD_DIR))
    return {"photos": names}
