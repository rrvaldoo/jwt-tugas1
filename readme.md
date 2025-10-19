# **MICROSERVICE PYTHON FLASK \+ JWT**

Aplikasi ini mendemonstrasikan arsitektur *microservice* dasar menggunakan **Python Flask** untuk tiga layanan yang berbeda, dengan otentikasi terpusat menggunakan **JWT (JSON Web Token)**.

## **ARSITEKTUR LAYANAN**

1. **Auth Service** (Port 5000): Bertanggung jawab untuk registrasi, login, dan menerbitkan JWT (token akses).  
2. **User Service** (Port 5001): Layanan terlindungi yang memerlukan JWT valid untuk diakses (simulasi pengambilan data pengguna).  
3. **Product Service** (Port 5002): Layanan terlindungi yang memerlukan JWT valid untuk diakses (simulasi pengambilan daftar produk).

Semua layanan berbagi JWT\_SECRET\_KEY yang sama untuk memverifikasi keaslian token yang diterbitkan oleh Auth Service.

## **PRA-SYARAT**

Pastikan Anda telah menginstal:

* Python 3.x  
* pip (Pengelola paket Python)  
* Postman atau cURL (untuk pengujian API)

## **LANGKAH INSTALASI & PERSIAPAN**

Karena ini adalah simulasi, kami akan berasumsi ketiga file aplikasi (auth\_service/app.py, user\_service/app.py, product\_service/app.py) dan file requirements.txt sudah tersedia dalam struktur proyek yang benar.

1. Instalasi Dependensi:  
   Semua layanan memerlukan Flask dan Flask-JWT-Extended.  
   \# Ini harus dijalankan di direktori setiap service  
   pip install Flask Flask-JWT-Extended

2. Menjalankan Ketiga Layanan:  
   Buka tiga terminal terpisah dan jalankan setiap layanan di port yang berbeda:

| Layanan | Direktori | Perintah Menjalankan | Port |
| :---- | :---- | :---- | :---- |
| **Auth Service** | auth\_service/ | python app.py | 5000 |
| **User Service** | user\_service/ | python app.py | 5001 |
| **Product Service** | product\_service/ | python app.py | 5002 |

## **PANDUAN PENGUJIAN API**

Ikuti langkah-langkah di bawah ini secara berurutan untuk menguji alur otentikasi:

### **LANGKAH 1: LOGIN (Mendapatkan Token)**

Tujuan: Mengirim kredensial ke Auth Service dan menerima JWT (token akses).

#### **Postman**

* **Metode:** POST  
* **URL:** http://127.0.0.1:5000/login  
* **Header:** Content-Type: application/json  
* **Body (raw, JSON):**  
  {  
      "username": "user1",  
      "password": "pass123"  
  }

* **Aksi:** Salin nilai dari kunci access\_token yang ada pada respons yang berhasil.

#### **cURL**

curl \-X POST \[http://127.0.0.1:5000/login\](http://127.0.0.1:5000/login) \\  
     \-H "Content-Type: application/json" \\  
     \-d '{"username": "user1", "password": "pass123"}'

**Respons Berhasil:**

{  
    "access\_token": "eyJhbGciOiJIUzI1Ni..."  
}

### **LANGKAH 2: AKSES USER SERVICE (Endpoint Terlindungi)**

Tujuan: Mengakses User Service menggunakan token yang diperoleh dari Langkah 1\.

#### **Postman**

* **Metode:** GET  
* **URL:** http://127.0.0.1:5001/users  
* **Authorization:** Pilih tipe **Bearer Token**.  
* **Token:** Tempelkan nilai access\_token dari Langkah 1\.

#### **cURL**

Ganti \<TOKEN\_JWT\> dengan token yang telah Anda salin.

curl \-X GET \[http://127.0.0.1:5001/users\](http://127.0.0.1:5001/users) \\  
     \-H "Authorization: Bearer \<TOKEN\_JWT\>"

**Respons Berhasil:**

{  
    "data": "Ini adalah data terlindungi dari User Service.",  
    "msg": "Selamat datang, user1\!"  
}

### **LANGKAH 3: AKSES PRODUCT SERVICE (Endpoint Terlindungi)**

Tujuan: Mengakses Product Service menggunakan token yang sama.

#### **Postman (Metode GET)**

* **Metode:** GET  
* **URL:** http://127.0.0.1:5002/products  
* **Authorization:** Pilih tipe **Bearer Token**.  
* **Token:** Tempelkan nilai access\_token dari Langkah 1\.

#### **cURL**

Ganti \<TOKEN\_JWT\> dengan token yang telah Anda salin.

curl \-X GET \[http://127.0.0.1:5002/products\](http://127.0.0.1:5002/products) \\  
     \-H "Authorization: Bearer \<TOKEN\_JWT\>"

**Respons Berhasil:**

{  
    "msg": "Daftar produk berhasil diambil oleh user: user1",  
    "products": \[  
        {"id": 1, "name": "Laptop XYZ", "price": 15000000},  
        ...  
    \]  
}

### **PENGUJIAN GAGAL (Tanpa Token)**

Jika Anda mencoba mengakses endpoint terlindungi (misalnya /products) tanpa menyertakan Authorization: Bearer \<TOKEN\>, Anda akan menerima:

**Respons:**

{  
    "msg": "Missing Authorization Header"  
}

**Status Code:** 401 Unauthorized
