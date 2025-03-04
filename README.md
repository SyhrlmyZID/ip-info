# IP Info - Web Intelligence Tool

## 📌 Deskripsi
IP Info adalah alat berbasis Python untuk mengumpulkan informasi tentang domain atau website. Alat ini dapat digunakan untuk mendapatkan informasi berikut:

- Alamat IP (IPv4 & IPv6)
- Lokasi Geografis (Kota, Wilayah, Latitude, Longitude)
- Zona Waktu
- Penyedia Layanan Internet (ISP)
- Organisasi yang mengelola IP
- Informasi DNS (Name Server)

Proyek ini bersifat **open-source** dan dapat digunakan pada berbagai platform seperti **Linux, Windows, macOS, dan Termux**.

## 🚀 Instalasi
Sebelum menjalankan script, pastikan Anda sudah menginstal dependensi yang diperlukan.

### 1️⃣ Persyaratan
Python **3.x** harus terinstal di sistem Anda. 
Cek versi Python dengan perintah berikut:
```bash
python3 --version
```

### 2️⃣ Instalasi Dependensi
Jalankan perintah berikut untuk menginstal pustaka yang dibutuhkan:
```bash
pip install requests dnspython colorama
```

## 🛠 Cara Penggunaan
Jalankan perintah berikut sesuai dengan sistem operasi yang digunakan.

### 🔹 Linux & macOS
```bash
python3 main.py example.com
```

### 🔹 Windows (Command Prompt / PowerShell)
```powershell
python main.py example.com
```

### 🔹 Termux (Android)
```bash
python main.py example.com
```

## 📌 Contoh Output
```bash
$ python3 main.py example.com

[Processing...]
==================================================
Hasil Pemeriksaan:
==================================================
IP Address:
  IPv4: 93.184.216.34
  IPv6: Not Available

Informasi Geografis:
  City: Los Angeles
  Region: California
  Latitude: 34.0522
  Longitude: -118.2437
  Time Zone: America/Los_Angeles
  ISP: Edgecast Inc.
  Organization: Verizon Digital Media
  AS: AS15133 Verizon Digital Media Services

DNS Information:
  Name Server 1: ns1.example.com
  Name Server 2: ns2.example.com
==================================================
Scan Selesai!
==================================================
```

## 🖼️ Screenshot
Berikut adalah tampilan saat menjalankan script:

![IP Info Screenshot](screenshot.png)

## 🛠 Kontribusi
Kami menerima kontribusi dari siapa saja yang ingin mengembangkan proyek ini lebih lanjut. Silakan **fork** repository ini dan buat **pull request** untuk menyarankan perubahan atau perbaikan.

## ⚖️ Lisensi
Proyek ini dilisensikan di bawah **MIT License**. Anda bebas menggunakannya dengan syarat mencantumkan atribusi yang sesuai.

---
✍️ Created by: [Your Name]

