from flask import Flask, render_template

app = Flask(__name__)

# Data Program Studi
prodi_data = {
    "nama": "Teknik Informatika",
    "fakultas": "Fakultas Ilmu Komputer",
    "jenjang": "S1",
    "akreditasi": "Unggul",
    "sk_akreditasi": "No. 4213/SK/BAN-PT/Akred/S/X/2025",
    "deskripsi": "Program Studi S1 Teknik Informatika berfokus pada pengembangan sistem cerdas, rekayasa perangkat lunak modern, keamanan jaringan, dan komputasi awan. Kami mendidik mahasiswa untuk menjadi profesional IT yang inovatif, berintegritas, dan mampu bersaing di tingkat global.",
    "visi": "Menjadi program studi unggul di tingkat internasional pada tahun 2030 dalam pengembangan teknologi informasi yang berdaya guna bagi masyarakat.",
    "misi": [
        "Menyelenggarakan pendidikan berkualitas tinggi berbasis kurikulum standar internasional di bidang Teknik Informatika.",
        "Melakukan penelitian inovatif yang berkontribusi pada pengembangan ilmu pengetahuan dan teknologi.",
        "Melakukan pengabdian kepada masyarakat melalui penerapan teknologi tepat guna untuk memecahkan masalah sosial.",
        "Membangun kemitraan strategis dengan industri nasional maupun global guna meningkatkan daya saing lulusan."
    ],
    "tujuan": [
        "Menghasilkan lulusan yang kompeten sebagai Software Engineer, Data Scientist, IT Consultant, atau Cyber Security Specialist.",
        "Menghasilkan karya ilmiah dan inovasi teknologi yang dipublikasikan secara nasional maupun internasional.",
        "Meningkatkan kemandirian masyarakat melalui program diseminasi teknologi informasi.",
        "Terjalinnya kolaborasi berkelanjutan dengan industri kelas dunia."
    ]
}

# Data Dosen (Minimal 3)
dosen_data = [
    {
        "nama": "Dr. Andi Wijaya, M.Kom",
        "nidn": "0011018801",
        "bidang": "Kecerdasan Buatan & Data Science",
        "email": "andi.wijaya@univ.ac.id",
        "pendidikan": "S3 Ilmu Komputer - Universitas Indonesia",
        "avatar": "https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&q=80&w=256&h=256"
    },
    {
        "nama": "Siti Rahayu, M.T",
        "nidn": "0025059002",
        "bidang": "Rekayasa Perangkat Lunak & Mobile Dev",
        "email": "siti.rahayu@univ.ac.id",
        "pendidikan": "S2 Teknik Informatika - Institut Teknologi Bandung",
        "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=256&h=256"
    },
    {
        "nama": "Budi Santoso, Ph.D",
        "nidn": "0017037703",
        "bidang": "Jaringan Komputer & Cloud Computing",
        "email": "budi.santoso@univ.ac.id",
        "pendidikan": "S3 Computer Science - Nanyang Technological University",
        "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&q=80&w=256&h=256"
    },
    {
        "nama": "Rahmat Hidayat, M.Cs",
        "nidn": "0012028904",
        "bidang": "Keamanan Siber & Kriptografi",
        "email": "rahmat.hidayat@univ.ac.id",
        "pendidikan": "S2 Ilmu Komputer - Universitas Gadjah Mada",
        "avatar": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&q=80&w=256&h=256"
    }
]

# Data Mahasiswa (Minimal 10 dengan berbagai status)
mahasiswa_data = [
    {"nim": "2021001", "nama": "Ahmad Fauzi", "angkatan": 2021, "status": "Aktif"},
    {"nim": "2021002", "nama": "Dewi Lestari", "angkatan": 2021, "status": "Aktif"},
    {"nim": "2020003", "nama": "Rudi Hartono", "angkatan": 2020, "status": "Cuti"},
    {"nim": "2021004", "nama": "Siti Aminah", "angkatan": 2021, "status": "Aktif"},
    {"nim": "2019005", "nama": "Bambang Pamungkas", "angkatan": 2019, "status": "Lulus"},
    {"nim": "2022006", "nama": "Citra Kirana", "angkatan": 2022, "status": "Aktif"},
    {"nim": "2022007", "nama": "Dian Sastro", "angkatan": 2022, "status": "Aktif"},
    {"nim": "2020008", "nama": "Eko Prasetyo", "angkatan": 2020, "status": "Tidak Aktif"},
    {"nim": "2021009", "nama": "Fajar Nusantara", "angkatan": 2021, "status": "Cuti"},
    {"nim": "2019010", "nama": "Gita Gutawa", "angkatan": 2019, "status": "Lulus"},
    {"nim": "2022011", "nama": "Hendra Wijaya", "angkatan": 2022, "status": "Aktif"},
    {"nim": "2020012", "nama": "Indah Permatasari", "angkatan": 2020, "status": "Tidak Aktif"}
]

@app.route("/")
def home():
    # Show dynamic stats and details
    stats = {
        "akreditasi": prodi_data["akreditasi"],
        "total_dosen": len(dosen_data),
        "total_mahasiswa": len(mahasiswa_data),
        "jenjang": prodi_data["jenjang"]
    }
    return render_template("home.html", prodi=prodi_data, stats=stats)

@app.route("/profil")
def profil():
    return render_template("profil.html", prodi=prodi_data)

@app.route("/dosen")
def dosen_list():
    return render_template("dosen.html", dosen=dosen_data)

@app.route("/mahasiswa")
def mahasiswa_list():
    return render_template("mahasiswa.html", mahasiswa=mahasiswa_data)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
