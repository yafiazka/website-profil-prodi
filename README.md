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

Berikut adalah susunan file dalam proyek ini beserta penjelasan fungsi masing-masing komponen:

```
website-profil-prodi/
│
├── app.py                  # File utama python (konfigurasi Flask, routing, data dummy)
├── README.md               # Dokumentasi panduan proyek
├── planning.md             # File rencana awal tugas kuliah
│
├── static/                 # Folder penyimpanan aset tambahan (CSS, JS, Gambar)
│   ├── css/
│   │   └── .gitkeep
│   └── img/
│       └── .gitkeep
│
└── templates/              # Berisi semua template halaman HTML (Jinja2)
    ├── base.html           # Template induk (berisi navbar responsif, footer, script library)
    ├── home.html           # Halaman Utama (dilengkapi hero section & ringkasan statistik prodi)
    ├── profil.html         # Halaman Profil (menampilkan deskripsi umum, visi, misi, dan tujuan prodi)
    ├── dosen.html          # Halaman Daftar Dosen (menampilkan kartu profil dosen beserta NIDN dan email)
    └── mahasiswa.html      # Halaman Daftar Mahasiswa (tabel status mahasiswa dengan badge warna & filter pencarian)
```

### Penjelasan Folder & File Utama:
1. **`app.py`**: Berfungsi sebagai *controller* dan *entrypoint* aplikasi. Di sinilah Flask diinisialisasi, rute URL (`/`, `/profil`, `/dosen`, `/mahasiswa`) ditentukan, dan data model (seperti data program studi, dosen, dan mahasiswa) disimpan dalam bentuk struktur data Python (dictionary/list) sebelum dikirim ke template HTML untuk di-render.
2. **`templates/`**: Folder wajib Flask untuk menyimpan template HTML. Flask secara otomatis mencari file HTML di dalam folder ini ketika memanggil fungsi `render_template()`.
3. **`static/`**: Folder wajib Flask untuk menyimpan file statik seperti gambar (`img/`), file CSS kustom (`css/`), atau JavaScript eksternal yang tidak diproses secara dinamis oleh backend Python.
4. **`.venv/`**: Lingkungan virtual (virtual environment) Python yang digunakan untuk mengisolasi instalasi dependencies (seperti Flask) agar tidak mengotori modul Python global pada sistem operasi.

---

## Fungsi dan Peran HTML Utama

Setiap file di dalam direktori `templates/` memiliki peran penting dalam arsitektur website ini:

1. **[base.html](file:///Users/yafiazka/Sites/localhost/website-profil-prodi/templates/base.html)** (*Template Induk / Base Layout*):
   - **Peran**: Menyediakan kerangka dasar HTML (tag `<html>`, `<head>`, `<body>`) yang digunakan oleh seluruh halaman.
   - **Fungsi**: Memuat CDN Tailwind CSS, pustaka ikon (Lucide Icons), font Google Fonts, serta mendefinisikan komponen global seperti **Header (Navbar responsif)** dan **Footer**. Template ini memiliki deklarasi `{% block content %}{% endblock %}` untuk menyisipkan konten dinamis dari halaman anak.
   
2. **[home.html](file:///Users/yafiazka/Sites/localhost/website-profil-prodi/templates/home.html)** (*Halaman Beranda*):
   - **Peran**: Halaman utama yang pertama kali dilihat oleh pengunjung (`/`).
   - **Fungsi**: Menampilkan panel visual sambutan (Hero Section) dengan animasi modern, visualisasi mock up kode program studi, serta ringkasan statistik (jumlah mahasiswa, jumlah dosen, akreditasi) yang di-render secara dinamis dari server.

3. **[profil.html](file:///Users/yafiazka/Sites/localhost/website-profil-prodi/templates/profil.html)** (*Halaman Profil Program Studi*):
   - **Peran**: Menyajikan profil mendalam mengenai program studi (`/profil`).
   - **Fungsi**: Menampilkan detail nama prodi, akreditasi beserta nomor SK resmi, deskripsi lengkap, serta daftar Visi, Misi, dan Tujuan program studi secara terstruktur menggunakan card.

4. **[dosen.html](file:///Users/yafiazka/Sites/localhost/website-profil-prodi/templates/dosen.html)** (*Halaman Daftar Dosen*):
   - **Peran**: Halaman informasi tenaga pendidik (`/dosen`).
   - **Fungsi**: Menampilkan daftar dosen pengajar dalam bentuk Grid Card yang modern. Dilengkapi dengan foto profil dosen, NIDN, bidang keahlian, riwayat pendidikan terakhir, serta tombol aksi cepat untuk mengirim email ke masing-masing dosen.

5. **[mahasiswa.html](file:///Users/yafiazka/Sites/localhost/website-profil-prodi/templates/mahasiswa.html)** (*Halaman Daftar Mahasiswa*):
   - **Peran**: Halaman data akademik mahasiswa (`/mahasiswa`).
   - **Fungsi**: Menyajikan daftar mahasiswa terdaftar dalam format tabel interaktif. Di halaman ini juga disematkan JavaScript untuk melakukan pencarian nama/NIM dan pemfilteran berdasarkan status akademik (Aktif, Cuti, Lulus, Tidak Aktif) secara real-time di sisi klien tanpa perlu reload halaman.

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

## Implementasi Konsep Jinja2 (Dynamic Templating)

Di bawah ini adalah penjelasan mendalam beserta contoh kode implementasi fitur-fitur mesin template Jinja2 pada proyek ini:

### 1. Konsep Pewarisan Template (Template Inheritance)

Template Inheritance memungkinkan kita membuat struktur halaman dasar (induk) dan menurunkan kerangka tersebut ke halaman-halaman lain (anak). Konsep ini menerapkan prinsip DRY (*Don't Repeat Yourself*).

- **Implementasi pada Template Induk (`templates/base.html`):**
  Di dalam `base.html`, kita menyiapkan slot kosong menggunakan tag `{% block %}`:
  ```html
  <title>{% block title %}{% endblock %} - S1 Teknik Informatika</title>
  ...
  <main class="flex-grow">
      {% block content %}{% endblock %}
  </main>
  ```

- **Implementasi pada Halaman Anak (Contoh: `templates/profil.html`):**
  Halaman anak menggunakan `{% extends "base.html" %}` di baris teratas untuk "mewarisi" struktur induk, lalu mengisi slot block yang bersangkutan:
  ```html
  {% extends "base.html" %}

  {% block title %}Profil Program Studi{% endblock %}

  {% block content %}
  <section class="bg-slate-900 text-white py-16 relative overflow-hidden">
      <!-- Isi konten profil prodi -->
  </section>
  {% endblock %}
  ```

---

### 2. Implementasi Variable Rendering

Variable Rendering adalah proses mencetak nilai variabel yang dikirim dari python backend (`app.py`) ke dalam dokumen HTML menggunakan sintaks double kurung kurawal `{{ ... }}`.

- **Pengiriman Variabel dari Backend (`app.py`):**
  ```python
  @app.route("/")
  def home():
      prodi_data = {
          "nama": "Teknik Informatika",
          "fakultas": "Fakultas Ilmu Komputer",
          # ...
      }
      return render_template("home.html", prodi=prodi_data)
  ```

- **Rendering Variabel di HTML (Contoh: `templates/profil.html`):**
  Variabel dicetak di template menggunakan sintaks `{{ nama_variabel.kunci }}` atau `{{ nama_variabel }}`:
  ```html
  <p class="text-slate-400">
      Kenali lebih dekat tentang S1 {{ prodi.nama }} {{ prodi.fakultas }}
  </p>
  ```
  Saat di-render oleh Flask, kode di atas akan menghasilkan output HTML statis seperti berikut:
  ```html
  <p class="text-slate-400">
      Kenali lebih dekat tentang S1 Teknik Informatika Fakultas Ilmu Komputer
  </p>
  ```

---

### 3. Implementasi For Loop (Perulangan)

Untuk menampilkan daftar data secara dinamis dari tipe data List atau Array di Python, kita menggunakan sintaks `{% for ... in ... %}` dan `{% endfor %}`.

- **Penggunaan di Template (`templates/profil.html`):**
  Untuk menampilkan daftar Misi dari `prodi.misi` (yang berupa list string):
  ```html
  <ul class="space-y-3">
      {% for item in prodi.misi %}
      <li class="flex items-start gap-2 text-sm text-slate-600">
          <span class="flex-shrink-0 w-5 h-5 rounded-full bg-violet-50 text-violet-600 flex items-center justify-center text-[10px] font-bold mt-0.5">
              {{ loop.index }}
          </span>
          <span>{{ item }}</span>
      </li>
      {% endfor %}
  </ul>
  ```
- **Detail Variabel Pendukung (`loop.index`):**
  `loop.index` adalah variabel bawaan Jinja2 yang berfungsi untuk melacak nomor urut iterasi saat ini (dimulai dari angka 1).

---

### 4. Implementasi If Statement (Logika Kondisional)

Logika kondisional digunakan untuk memanipulasi tampilan atau elemen HTML berdasarkan kriteria tertentu dengan menggunakan tag `{% if %}`, `{% elif %}`, `{% else %}`, dan `{% endif %}`.

- **Implementasi pada Badge Status Mahasiswa (`templates/mahasiswa.html`):**
  Kami membedakan warna dan bentuk badge status berdasarkan status masing-masing mahasiswa secara dinamis:
  ```html
  {% if mhs.status == 'Aktif' %}
  <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
      <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
      Aktif
  </span>
  {% elif mhs.status == 'Cuti' %}
  <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold bg-amber-50 text-amber-700 border border-amber-200">
      <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
      Cuti
  </span>
  {% elif mhs.status == 'Lulus' %}
  <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold bg-blue-50 text-blue-700 border border-blue-200">
      <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
      Lulus
  </span>
  {% else %}
  <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold bg-rose-50 text-rose-700 border border-rose-200">
      <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
      Tidak Aktif
  </span>
  {% endif %}
  ```
  Dengan kode di atas, jika status mahasiswa bernilai `'Aktif'`, badge berwarna hijau akan di-render. Jika `'Cuti'` berwarna kuning, jika `'Lulus'` berwarna biru, dan selain itu (status `'Tidak Aktif'`) berwarna merah.
