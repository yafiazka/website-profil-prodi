# Website Profil Program Studi S1 Teknik Informatika

Halo! Ini adalah proyek tugas kelompok untuk membangun website profil program studi S1 **Teknik Informatika** berbasis web. Website ini dibuat secara dinamis menggunakan **Flask** (Python) sebagai backend, **Jinja2** untuk manajemen template HTML, dan dihias menggunakan **Tailwind CSS** agar tampilannya modern dan responsif.

---

## Anggota Kelompok

_Silakan sesuaikan dengan nama dan NIM anggota kelompok:_

- **Muhammad Yafi Azka** - (NIM: 24210003)

---

## Teknologi & Fitur Utama

Dalam membuat website ini, kami menerapkan beberapa komponen penting:

- **Backend & Routing**: Menggunakan **Flask** untuk mengelola rute (URL) halaman dan membagikan data dummy ke tiap halaman.
- **Dynamic Templating**: Memanfaatkan **Jinja2** agar halaman HTML bisa menggunakan logic seperti pengulangan data (`for loop`), pengkondisian status (`if statement`), dan pewarisan template (`extends/block`).
- **Styling & Tampilan**: Menggunakan **Tailwind CSS** (via CDN) dengan palet warna modern indigo/violet, tipografi Google Fonts (_Plus Jakarta Sans_ & _Outfit_), serta ikon interaktif dari _Lucide Icons_.
- **Fitur Pencarian & Filter (Mahasiswa)**: Ditambahkan script Javascript sederhana di sisi klien agar pengguna bisa mencari nama/NIM mahasiswa dan memfilter status secara real-time langsung di tabel tanpa perlu reload halaman.

---

## Struktur Proyek

Berikut adalah susunan file dalam proyek ini:

```
website-profil-prodi/
│
├── app.py                  # File utama python (konfigurasi Flask, routing, data dummy)
├── README.md               # Dokumentasi panduan proyek
├── planning.md             # File rencana awal tugas kuliah
│
├── static/                 # Folder penyimpanan aset tambahan jika diperlukan
│   ├── css/
│   │   └── .gitkeep
│   └── img/
│       └── .gitkeep
│
└── templates/              # Berisi semua template halaman HTML
    ├── base.html           # Template induk (berisi navbar responsif, footer, script library)
    ├── home.html           # Halaman Utama (dilengkapi hero section & ringkasan statistik prodi)
    ├── profil.html         # Halaman Profil (menampilkan deskripsi umum, visi, misi, dan tujuan prodi)
    ├── dosen.html          # Halaman Daftar Dosen (menampilkan kartu profil dosen beserta NIDN dan email)
    └── mahasiswa.html      # Halaman Daftar Mahasiswa (tabel status mahasiswa dengan badge warna & filter pencarian)
```

---

## Cara Menjalankan Project

Silakan ikuti langkah-langkah berikut untuk menjalankan website di komputer lokal Anda:

### 1. Persiapan Awal

Pastikan komputer Anda sudah terinstal **Python 3**.

### 2. Instalasi Flask

Buka terminal atau command prompt (cmd), lalu instal library Flask dengan perintah:

```bash
pip install flask
```

### 3. Menjalankan Server

Masuk ke direktori folder proyek ini, kemudian jalankan server lokal:

```bash
python app.py
```

_Catatan: Secara default Flask akan berjalan di port `5000`._

### 4. Akses Website

Buka browser favorit Anda (Chrome/Firefox/Edge) lalu kunjungi alamat berikut:

```
http://127.0.0.1:5000/
```

---

## Implementasi Konsep Jinja2

Di bawah ini adalah penjelasan singkat bagaimana konsep Jinja2 kami terapkan di dalam kode:

1. **Pewarisan Template (Template Inheritance)**:
   Kami membuat kerangka dasar navbar dan footer di `base.html`. Halaman lain tinggal menggunakannya kembali dengan menulis `{% extends "base.html" %}` di baris paling atas dan membungkus isinya dengan `{% block content %}`.
2. **Variable Rendering**:
   Data dikirim langsung dari `app.py` dan ditampilkan di HTML menggunakan format double kurung kurawal `{{ prodi.nama }}`.
3. **Looping data (`{% for %}`)**:
   Kami melakukan perulangan untuk menampilkan daftar dosen di `dosen.html` dan tabel mahasiswa di `mahasiswa.html` secara dinamis dari list Python.
4. **Logika Kondisi (`{% if %}`)**:
   Pada halaman mahasiswa, warna badge status disesuaikan menggunakan percabangan Jinja:
   - Jika status `Aktif` -> badge warna Hijau 🟢
   - Jika status `Cuti` -> badge warna Kuning 🟡
   - Jika status `Lulus` -> badge warna Biru 🔵
   - Jika status `Tidak Aktif` -> badge warna Merah 🔴
