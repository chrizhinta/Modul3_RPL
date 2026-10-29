# Sistem Manajemen Perpustakaan

Aplikasi desktop manajemen perpustakaan berbasis **MVC (Model-View-Controller)** menggunakan Python, CustomTkinter, dan basis data MySQL.

## Fitur

- Login dengan password ter-hash SHA-256
- Otorisasi berbasis peran: `admin` dan `anggota`
- CRUD data buku (khusus admin), anggota hanya bisa melihat
- Logout kembali ke halaman login
- Unit test (pytest) dan CI otomatis dengan GitHub Actions

## Struktur Direktori

```text
Modul3_RPL/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
├── config/
│   └── database.py
├── controller/
│   ├── anggota_controller.py
│   ├── auth_controller.py
│   └── buku_controller.py
├── models/
│   ├── anggota_model.py
│   ├── buku_model.py
│   └── user_model.py
├── views/
│   ├── anggota_view.py
│   ├── buku_view.py
│   └── login_view.py
├── test/
│   ├── test_auth.py
│   └── test_buku.py
├── main.py
├── requirements.txt
└── README.md
```

## Panduan Instalasi dan Konfigurasi Database

### 1. Siapkan database MySQL

1. Buka **Laragon**, lalu klik **Start All**.
2. Buka terminal Laragon, lalu masuk ke MySQL:

   ```bash
   mysql -u root -p
   ```

3. Buat database:

   ```sql
   CREATE DATABASE db_modul3;
   USE db_modul3;
   ```

4. Buat tabel `users` dan isi akun uji coba:

   ```sql
   CREATE TABLE users (
       id_user INT PRIMARY KEY AUTO_INCREMENT,
       username VARCHAR(50) NOT NULL UNIQUE,
       password VARCHAR(255) NOT NULL,
       role ENUM('admin', 'anggota') NOT NULL DEFAULT 'anggota'
   );

   INSERT INTO users (username, password, role) VALUES
   ('petugas', SHA2('admin123', 256), 'admin'),
   ('mahasiswa', SHA2('user123', 256), 'anggota');
   ```

5. Buat tabel `buku` dan `anggota` sesuai modul praktikum sebelumnya.

### 2. Siapkan proyek

```bash
git clone https://github.com/chrizhinta/Modul3_RPL.git
cd Modul3_RPL
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

Pastikan pengaturan di `config/database.py` sesuai:

```python
self.host = "localhost"
self.db_name = "db_modul3"
self.username = "root"
self.password = ""
```

## Cara Menjalankan Aplikasi

1. Pastikan MySQL di Laragon sudah menyala.
2. Jalankan:

   ```bash
   python main.py
   ```

3. Login dengan akun uji coba:

   | Username  | Password | Role    | Hak akses                    |
   |-----------|----------|---------|------------------------------|
   | petugas   | admin123 | admin   | Simpan, Perbarui, Hapus buku |
   | mahasiswa | user123  | anggota | Hanya melihat daftar buku    |

### Menjalankan pengujian

```bash
python -m pytest -v
```

### Membuat berkas .exe

```bash
pyinstaller --noconfirm --onefile --windowed --name "AplikasiPerpustakaan" --collect-all mysql.connector --hidden-import mysql.connector.plugins.mysql_native_password --hidden-import mysql.connector.plugins.caching_sha2_password main.py
```

Hasilnya ada di `dist/AplikasiPerpustakaan.exe`. MySQL harus menyala sebelum aplikasi dibuka.