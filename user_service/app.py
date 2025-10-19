from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)
# Secret key harus sama atau setidaknya JWT Manager harus dikonfigurasi untuk memverifikasi token dari Auth Service
# Untuk contoh sederhana ini, kita samakan secret key-nya.
app.config["JWT_SECRET_KEY"] = "super-secret-key-auth"
jwt = JWTManager(app)

@app.route("/users", methods=["GET"])
@jwt_required()
def get_user_data():
    # Ambil identity dari JWT (yang merupakan 'username' dari Auth Service)
    current_user = get_jwt_identity()
    return jsonify({
        "msg": f"Selamat datang, {current_user}!",
        "data": "Ini adalah data terlindungi dari User Service."
    }), 200

if __name__ == "__main__":
    app.run(port=5001, debug=True)