from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)
# Secret key harus sama dengan Auth Service agar dapat memverifikasi token
app.config["JWT_SECRET_KEY"] = "super-secret-key-auth"
jwt = JWTManager(app)

# Data produk dummy
products_db = [
    {"id": 1, "name": "Laptop XYZ", "price": 15000000},
    {"id": 2, "name": "Smartphone ABC", "price": 8000000},
    {"id": 3, "name": "Monitor Ultra", "price": 4500000},
]

@app.route("/products", methods=["GET"])
@jwt_required()
def get_products():
    """Endpoint untuk mengambil semua daftar produk. Hanya bisa diakses dengan JWT valid."""
    current_user = get_jwt_identity() # Ambil identitas pengguna (username) dari token
    return jsonify({
        "msg": f"Daftar produk berhasil diambil oleh user: {current_user}",
        "products": products_db
    }), 200

if __name__ == "__main__":
    # Jalankan Product Service di port 5002
    app.run(port=5002, debug=True)