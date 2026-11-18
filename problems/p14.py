from flask import Flask, request, jsonify

app = Flask(__name__)
USERS = {
    "t1": {"name": "kim", "phone": "010-1111-2222"},
    "t2": {"name": "lee", "phone": "010-3333-4444"},
}
current_user = None


@app.route("/auth")
def auth():
    global current_user
    current_user = USERS.get(request.args.get("token"))
    return jsonify(ok=current_user is not None)


@app.route("/me")
def me():
    if current_user is None:
        return jsonify(error="login required"), 401
    return jsonify(current_user)
