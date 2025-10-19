from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, JWTManager

app = Flask(__name__)
# Ganti dengan secret key yang kuat di lingkungan produksi
app.config["JWT_SECRET_KEY"] = "super-secret-key-auth"
jwt = JWTManager(app)

# Database sederhana in-memory
users = {
    "user1": "pass123",
    "admin": "admin456"
}

@app.route("/register", methods=["POST"])
def register():
    # Simulasi register sederhana (hanya menambahkan ke dictionary)
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "Username dan password diperlukan"}), 400

    if username in users:
        return jsonify({"msg": "Username sudah ada"}), 409

    users[username] = password
    return jsonify({"msg": "Registrasi berhasil!"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)

    if username in users and users[username] == password:
        # Identity di sini akan menjadi 'username'
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Username atau password salah"}), 401

if __name__ == "__main__":
    app.run(port=5000, debug=True)