kuis = [
    {
        "no_soal": 1,
        "soal": "Apa yang dimaksud dengan algoritma?",
        "pilihan_jawaban": {
            "a": "Bahasa pemrograman",
            "b": "Langkah-langkah logis untuk menyelesaikan masalah",
            "c": "Aplikasi komputer",
            "d": "Sistem operasi"
        },
        "jawaban_benar": "b",
        "jawaban": "",
        "poin": 10
    },
    {
        "no_soal": 2,
        "soal": "Simbol flowchart yang digunakan untuk MULAI dan SELESAI adalah...",
        "pilihan_jawaban": {
            "a": "Persegi panjang",
            "b": "Jajar genjang",
            "c": "Oval",
            "d": "Belah ketupat"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10
    },
    {
        "no_soal": 3,
        "soal": "Tipe data untuk menyimpan angka desimal adalah...",
        "pilihan_jawaban": {
            "a": "int",
            "b": "str",
            "c": "float",
            "d": "bool"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10
    },
    {
        "no_soal": 4,
        "soal": "Operator yang digunakan untuk pembagian sisa (modulus) di Python adalah...",
        "pilihan_jawaban": {
            "a": "/",
            "b": "//",
            "c": "%",
            "d": "**"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10
    },
    {
        "no_soal": 5,
        "soal": "Apa fungsi dari perintah input() di Python?",
        "pilihan_jawaban": {
            "a": "Menampilkan output ke layar",
            "b": "Mengambil data dari database",
            "c": "Menerima input dari pengguna",
            "d": "Menghapus data"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10
    },
    {
        "no_soal": 6,
        "soal": "Struktur percabangan di Python menggunakan kata kunci...",
        "pilihan_jawaban": {
            "a": "for",
            "b": "while",
            "c": "if",
            "d": "def"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10
    },
    {
        "no_soal": 7,
        "soal": "Perulangan yang digunakan saat jumlah perulangan sudah diketahui adalah...",
        "pilihan_jawaban": {
            "a": "if",
            "b": "while",
            "c": "for",
            "d": "def"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10
    },
    {
        "no_soal": 8,
        "soal": "Fungsi dari keyword def pada Python adalah untuk...",
        "pilihan_jawaban": {
            "a": "Mendeklarasikan variabel",
            "b": "Mendefinisikan fungsi",
            "c": "Membuat perulangan",
            "d": "Menjalankan program"
        },
        "jawaban_benar": "b",
        "jawaban": "",
        "poin": 10
    },
    {
        "no_soal": 9,
        "soal": "Struktur data yang dapat menyimpan banyak data dalam satu variabel di Python adalah...",
        "pilihan_jawaban": {
            "a": "int",
            "b": "float",
            "c": "list",
            "d": "bool"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10
    },
    {
        "no_soal": 10,
        "soal": "Apa output dari kode berikut?\nprint(2 ** 3)",
        "pilihan_jawaban": {
            "a": "5",
            "b": "6",
            "c": "8",
            "d": "9"
        },
        "jawaban_benar": "c",
        "jawaban": "",
        "poin": 10
    }
]

is_submit = True

def hitung_skor(kuis):
    skor = 0
    for soal in kuis:
        if soal["jawaban"] == soal["jawaban_benar"]:
            skor += soal["poin"]
    return skor

def tampilkan_hasil(kuis, skor_total):
    print("\n" + "="*60)
    print("Hasil Kuis")
    print("="*60)
    
    for soal in kuis:
        no_soal = soal["no_soal"]
        pertanyaan = soal["soal"]
        jawaban_user = soal["jawaban"].upper()
        jawaban_benar = soal["jawaban_benar"].upper()
        poin = soal["poin"]
        
        if jawaban_user == jawaban_benar:
            ikon = "✅"
        else:
            ikon = "❌"

        print(f"{ikon} Soal {no_soal}: {pertanyaan}")
        print(f"=> Jawaban kamu  : {jawaban_user}")
        print(f"=> Jawaban benar : {jawaban_benar}")
        print(f"=> Poin          : {poin if ikon == '✅' else 0}/{poin}")
        print("-" * 60)

    total_maksimal = sum(soal["poin"] for soal in kuis)
    print(f"\nSkor Akhir: {skor_total} / {total_maksimal} poin")
    persentase = (skor_total / total_maksimal) * 100
    print(f"Persentase benar: {persentase:.1f}%")
    print("="*60)

print(f"Terdapat {len(kuis)} soal. Selamat Mengerjakan!\n")

# Tanya satu per satu
for soal in kuis:
    print(f"Soal {soal['no_soal']}/{len(kuis)} [{soal['poin']} poin]")
    print(f"{soal['soal']}")
    
    for key, value in soal['pilihan_jawaban'].items():
        print(f"{key}) {value}")
    
    while True:
        jawaban_kamu = input("\nJawaban kamu (a/b/c/d): ").lower()
        if jawaban_kamu in ['a', 'b', 'c', 'd']:
            soal["jawaban"] = jawaban_kamu
            print(f"Terpilih: {jawaban_kamu.upper()}\n")
            break
        else:
            print("Pilihlah jawaban a, b, c, atau d!")

# Konfirmasi submit
while is_submit:
    if input("Ketik 'submit' untuk melihat hasil: ").lower() != "submit":
         continue
    else:
        is_submit = False
        skor = hitung_skor(kuis)
        tampilkan_hasil(kuis, skor)