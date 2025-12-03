# import library yang dibutuhkan
from datetime import datetime
import random
import json

# buka soal kuis 
with open('soal.json', 'r', encoding='utf-8') as file:
    kuis = json.load(file)

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
        print(f"{ikon} {no_soal}. {soal['soal']}")
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
    print("=" * 60)
    print(f"Selamat Datang di Kuis")
    print("=" * 60)
    # variabel input nama, nim, dan kategori soal
    nama = input("Masukkan Nama Lengkap: ")
    nim = input("Masukkan NIM: ")
    kategori_soal = input("Masukkan Kategori Soal [DSP/LGA]: ")
    # validasi input nama dan nim tidak boleh kosong
    if kategori_soal.lower() not in ["dsp", "lga"]:
        print("❗ Kategori soal tidak valid! Pilih kategori yang tersedia.\n")
    # jika kategori soal tidak sesuai, tampilkan pesan kesalahan
    elif nama.strip() ==  "" or nim == "" or kategori_soal.strip() == "":
        print("❗ Nama, NIM, dan Kategori Soal tidak boleh kosong!\n")
    # jika tidak kosong, jalankan fungsi main untuk memulai kuis
    else:
        print(f"\nTerpilih Soal {kategori_soal.upper()}. Selamat Mengerjakan, {nama}!\n")
        main()
        break
    
# loop untuk submit kuis atau ganti jawaban
while True:
    # input untuk submit kuis atau ganti jawaban
    submit = input("\nMasukkan no soal untuk mengganti jawaban atau 'submit' untuk mengirim: ").strip().lower()
    # kalau ketik 'submit' untuk mengirim
    if submit == "submit":
        skor = hitung_skor(kuis_berdasarkan_kategori)
        tampilkan_hasil(kuis_berdasarkan_kategori, skor)
        break
    # kalau ketik angka (nomor soal) untuk mengganti jawaban
    elif submit.isdigit():
        nomor = int(submit)
        if 1 <= nomor <= len(kuis_berdasarkan_kategori):
            soal = kuis_berdasarkan_kategori[nomor-1]  # index mulai dari 0
            print(f"\nRevisi Jawaban - Soal {nomor}")
            print(f"{soal['soal']}")
            for key, value in soal['pilihan_jawaban'].items():
                print(f"  {key}) {value}")
            print(f"Jawaban sebelumnya: {soal['jawaban'].upper() if soal['jawaban'] else 'Belum dijawab'}")
            # loop jawaban untuk validasi input jawaban baru
            while True:
                jawab_baru = input("\nJawaban baru (a/b/c/d): ").lower().strip()
                if jawab_baru in ['a', 'b', 'c', 'd']:
                    soal["jawaban"] = jawab_baru
                    print(f"Jawaban diubah menjadi: {jawab_baru.upper()}\n")
                    break
                else:
                    print("Pilih jawaban a, b, c, atau d!")
        else:
            print(f"Nomor soal tidak tersedia! Pilih 1 sampai {len(kuis_berdasarkan_kategori)}")
    else:
        print("Ketik nomor soal atau 'submit'!")