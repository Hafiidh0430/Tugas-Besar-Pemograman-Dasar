from datetime import datetime
import random

# soal kuis 
kuis = [
    {
        "soal": "Apa yang dimaksud dengan algoritma?",
        "pilihan_jawaban": {
            "a": "Bahasa pemrograman",
            "b": "Langkah-langkah logis untuk menyelesaikan masalah",
            "c": "Aplikasi komputer",
            "d": "Sistem operasi"
        },
        "jawaban_benar": "b",
        "jawaban": "",
        "poin": 10,
        "kategori_soal": "Logika Algoritma"
    },
    {
        "soal": "Simbol flowchart yang digunakan untuk MULAI dan SELESAI adalah...",
        "pilihan_jawaban": {
            "a": "Persegi panjang",
            "b": "Jajar genjang",
            "c": "Oval",
            "d": "Belah ketupat"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10,
        "kategori_soal": "Logika Algoritma"
    },
    {
        "soal": "Tipe data untuk menyimpan angka desimal adalah...",
        "pilihan_jawaban": {
            "a": "int",
            "b": "str",
            "c": "float",
            "d": "bool"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10,
        "kategori_soal": "Logika Algoritma"
    },
    {
        "soal": "Operator yang digunakan untuk pembagian sisa (modulus) di Python adalah...",
        "pilihan_jawaban": {
            "a": "/",
            "b": "//",
            "c": "%",
            "d": "**"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10,
        "kategori_soal": "Logika Algoritma"
    },
    {
        "soal": "Apa fungsi dari perintah input() di Python?",
        "pilihan_jawaban": {
            "a": "Menampilkan output ke layar",
            "b": "Mengambil data dari database",
            "c": "Menerima input dari pengguna",
            "d": "Menghapus data"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10,
        "kategori_soal": "Logika Algoritma"
    },
    {
        "soal": "Struktur percabangan di Python menggunakan kata kunci...",
        "pilihan_jawaban": {
            "a": "for",
            "b": "while",
            "c": "if",
            "d": "def"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10,
        "kategori_soal": "Dasar Pemrograman"
    },
    {
        "soal": "Perulangan yang digunakan saat jumlah perulangan sudah diketahui adalah...",
        "pilihan_jawaban": {
            "a": "if",
            "b": "while",
            "c": "for",
            "d": "def"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10,
        "kategori_soal": "Dasar Pemrograman"
    },
    {
        "soal": "Fungsi dari keyword def pada Python adalah untuk...",
        "pilihan_jawaban": {
            "a": "Mendeklarasikan variabel",
            "b": "Mendefinisikan fungsi",
            "c": "Membuat perulangan",
            "d": "Menjalankan program"
        },
        "jawaban_benar": "b",
        "jawaban": "",
        "poin": 10,
        "kategori_soal": "Dasar Pemrograman"
    },
    {
        "soal": "Struktur data yang dapat menyimpan banyak data dalam satu variabel di Python adalah...",
        "pilihan_jawaban": {
            "a": "int",
            "b": "float",
            "c": "list",
            "d": "bool"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10,
        "kategori_soal": "Dasar Pemrograman"
    },
    {
    
        "soal": "Apa output dari kode berikut?\nprint(2 ** 3)",
        "pilihan_jawaban": {
            "a": "5",
            "b": "6",
            "c": "8",
            "d": "9"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10,
        "kategori_soal": "Dasar Pemrograman"
    }
]

# global variabel untuk menyimpan data user
nama, nim, kategori_soal = "", "", ""

# filter kuis berdasarkan kategori soal
kuis_berdasarkan_kategori = []

# fungsi untuk menampilkan tanggal
def tampilkan_tanggal():
    # inisialisasi tanggal sekarang
    sekarang = datetime.now()
    # format tanggal menjadi dd-mm-yyyy
    tanggal_format = sekarang.strftime("%d-%m-%Y")
    # tampilkan tanggal
    print(f"Tanggal & Waktu  : {tanggal_format} - {sekarang.strftime('%H:%M:%S') }")

# fungsi untuk hitung skor hasil kuis
def hitung_skor(kuis):
    # inisialisasi skor
    skor = 0
    # loop soal kuis dan hitung skor
    for soal in kuis:
        # jika jawabannya benar, tambah skor dari poin soal
        if soal["jawaban"] == soal["jawaban_benar"]:
            skor += soal["poin"]
    # return skor 
    return skor

# fungsi untuk menampilkan hasil kuis
def tampilkan_hasil(kuis_berdasarkan_kategori, skor_total):
    print("\n" + "=" * 60)
    print("Hasil Kuis")
    print("=" * 60)
    # loop soal kuis 
    for no_soal, soal in enumerate(kuis_berdasarkan_kategori, start=1):
        # inisialisasi variabel no soal, pertanyaan, jawaban user, jawaban benar, dan poin
        jawaban_kamu = soal["jawaban"].upper()
        jawaban_benar = soal["jawaban_benar"].upper()
        poin = soal["poin"]
        # jika jawaban kamu sama dengan jawaban benar pada soal, maka ganti ikon
        ikon = "✅" if jawaban_kamu == jawaban_benar else "❌"
        # tampilkan hasil per soal dengan jawaban
        print(f"{ikon} Soal: {no_soal}. {soal['soal']}")
        print(f"=> Jawaban kamu  : {jawaban_kamu}")
        print(f"=> Jawaban benar : {jawaban_benar}")
        print(f"=> Poin          : {poin if ikon == '✅' else 0}/{poin}")
        print("-" * 60)

    # hitung dan tampilkan total maksimal dari seluruh poin
    total_maksimal = sum(soal["poin"] for soal in kuis_berdasarkan_kategori)
    print(f"\nSkor Akhir: {skor_total} / {total_maksimal} poin")
    # hitung dan tampilkan persentase skor dan grade
    persentase = (skor_total / total_maksimal) * 100
    grades = ["F", "F", "F", "F", "E", "D", "C", "B", "A", "A", "A"]
    grade = grades[min(int(persentase // 10), 10)]
    
    print(f"Persentase benar: {persentase:.1f}% ({grade})")
    tampilkan_tanggal()
    print("=" * 60)

# fungsi utama untuk menjalankan kuis
def main():
    # mulai kuis
    print(f"\nTerdapat {len(kuis_berdasarkan_kategori)} soal. Selamat Mengerjakan!\n")
    # loop untuk memfilter soal berdasarkan kategori
    for soal in kuis:
        if soal["kategori_soal"].lower() == kategori_soal.lower():
            kuis_berdasarkan_kategori.append(soal)
    # loop soal kuis yg sudah di filter berdasarkan kategori dan kita random urutannya 
    random.shuffle(kuis_berdasarkan_kategori)
    for no_soal, soal in enumerate(kuis_berdasarkan_kategori, start=1):
        # tampilkan soal
        print(f"Soal {no_soal}/{len(kuis_berdasarkan_kategori)} [{soal['poin']} poin]")
        print(f"{soal['soal']}")
        # tampilkan pilihan jawaban
        for key, value in soal['pilihan_jawaban'].items():
            print(f"{key}) {value}")
        # loop true untuk validasi input jawaban (a/b/c/d)
        while True:
            # inisialisasi input jawaban kamu
            jawaban_kamu = input("\nJawaban kamu (a/b/c/d): ").lower()
            # jika jawaban kamu menjawab (a/b/c/d), simpan jawaban dan keluar dari loop
            if jawaban_kamu in ['a', 'b', 'c', 'd']:
                soal["jawaban"] = jawaban_kamu
                print(f"Terpilih: {jawaban_kamu.upper()}\n")
                break
            # jika tidak sesuai, tampilkan pesan kesalahan
            else:
                print("❗ Pilihlah jawaban a, b, c, atau d!")

# loop input data user untuk memulai kuis
while True:
    # variabel input nama, nim, dan kategori soal
    nama = input("Masukkan Nama Lengkap: ")
    nim = input("Masukkan NIM: ")
    kategori_soal = input("Masukkan Kategori Soal [Dasar Pemrograman/Logika Algoritma]: ")
    
    # validasi input nama dan nim tidak boleh kosong
    if kategori_soal.lower() not in ["dasar pemrograman", "logika algoritma"]:
        print("❗ Kategori soal tidak valid! Pilih kategori yang tersedia.\n")
    # jika kategori soal tidak sesuai, tampilkan pesan kesalahan
    elif nama.strip() ==  "" or nim == "" or kategori_soal.strip() == "":
        print("❗ Nama, NIM, dan Kategori Soal tidak boleh kosong!\n")
    # jika tidak kosong, jalankan fungsi main untuk memulai kuis
    else:
        main()
        break
    
# loop submit untuk melihat hasil kuis
while True:
    # jika input bukan 'submit', ulangi loop
    if input("Ketik 'submit' untuk melihat hasil: ").lower() != "submit":
           print("❗ Tolong ketik 'submit untuk mengirim kuis!")
    # jika input 'submit', hitung skor dan tampilkan hasil
    else:
        skor = hitung_skor(kuis_berdasarkan_kategori)
        tampilkan_hasil(kuis_berdasarkan_kategori, skor)
        break