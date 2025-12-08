# import library
from datetime import datetime # untuk ambil tanggal & waktu
import random # untuk mengacak soal
import json # untuk membaca file JSON

# baca file dari soal.json
with open('soal.json', 'r', encoding='utf-8') as file:
    kuis = json.load(file) # load seluruh soal dari file JSON

# global variabel 
nama, nim, kategori_soal = "", "", "" # menyimpan info user
kuis_berdasarkan_kategori = [] # menampung soal sesuai kategori user

# fungsi tampilkan tanggal & waktu
def tampilkan_tanggal():
    sekarang = datetime.now()
    tanggal_format = sekarang.strftime("%d-%m-%Y")
    print(f"Tanggal & Waktu : {tanggal_format} - {sekarang.strftime('%H:%M:%S')}")

# fungsi hitung skor akhir
def hitung_skor(kuis):
    skor = 0
    for soal in kuis:
        if soal["jawaban"] == soal["jawaban_benar"]: # cek benar/tidak
            skor += soal["poin"] # tambahkan poin
    return skor

# fungsi tampilkan hasil akhir kuis
def tampilkan_hasil(kuis_berdasarkan_kategori, skor_total):
    print("\n" + "=" * 60)
    print("Hasil Kuis")
    print("=" * 60)

    # tampilkan tiap soal + status benar/salah
    for no_soal, soal in enumerate(kuis_berdasarkan_kategori, start=1):
        jawaban_kamu = soal["jawaban"].upper()
        jawaban_benar = soal["jawaban_benar"].upper()
        poin = soal["poin"]

        ikon = "✅" if jawaban_kamu == jawaban_benar else "❌"

        print(f"{ikon} {no_soal}. {soal['soal']}")
        print(f"=> Jawaban kamu : {jawaban_kamu}")
        print(f"=> Jawaban benar : {jawaban_benar}")
        print(f"=> Poin : {poin if ikon == '✅' else 0}/{poin}")
        print("-" * 60)

    # hitung nilai akhir & persentase
    total_maksimal = sum(soal["poin"] for soal in kuis_berdasarkan_kategori)
    print(f"\nSkor Akhir: {skor_total} / {total_maksimal} poin")

    persentase = (skor_total / total_maksimal) * 100

    # convert persentase menjadi grade
    grades = ["F","F","F","F","E","D","C","B","A","A","A"]
    grade = grades[min(int(persentase // 10), 10)]
    print(f"Persentase benar: {persentase:.1f}% ({grade})")

    tampilkan_tanggal()
    print("=" * 60)

# navigasi nomor-nomor soal
def tampilkan_navigasi():
    bar = "" # string tampilan navigasi

    # loop setiap soal
    for i, soal in enumerate(kuis_berdasarkan_kategori):
        # tampilkan nomor soal jika belum dijawab
        if soal['jawaban'] == "":
            bar += f"[{i+1}] "
        # tamplilkan tanda centang jika soal sudah dijawab
        else:
            bar += f"[✓] "

    print("\n" + bar + "\n")

# fungsi utama untuk kuis
def main():

    # filter soal berdasarkan kategori user
    for soal in kuis:
        if soal["kategori_soal"].lower() == kategori_soal.lower():
            kuis_berdasarkan_kategori.append(soal)

    random.shuffle(kuis_berdasarkan_kategori) # acak urutan soal

    index = 0 # index sebagai pointer nomor soal saat ini
    
    # loop selama masih ada soal
    while index < len(kuis_berdasarkan_kategori):

        soal = kuis_berdasarkan_kategori[index] # soal aktif
        no_soal = index + 1 # nomor soal real

        tampilkan_navigasi() # tampilkan navigasi di atas soal

        print(f"Soal {no_soal}/{len(kuis_berdasarkan_kategori)} [{soal['poin']} poin]")
        print(soal['soal'])

        # tampilkan opsi jawaban
        for key, value in soal["pilihan_jawaban"].items():
            print(f"{key}) {value}")

        while True:
            pilihan = input("\nJawaban kamu (a/b/c/d) atau nomor soal lain: ").lower().strip()

            # jika input angka → pindah soal
            if pilihan.isdigit():
                nomor = int(pilihan)
                if 1 <= nomor <= len(kuis_berdasarkan_kategori):
                    print(f"\n=> Pindah ke soal {nomor}...\n")
                    index = nomor - 1 # update pointer soal
                    break
                else:
                    print("❗ Nomor tidak valid!")
                    continue

            # kalau jawabannya a/b/c/d, maka simpan jawaban
            if pilihan in ['a','b','c','d']:
                soal["jawaban"] = pilihan
                print(f"Terpilih: {pilihan.upper()}\n")
                index += 1 # lanjut ke soal berikutnya
                break

            print("❗ Pilih a/b/c/d atau nomor soal!")

# input data user
while True:
    print("=" * 60)
    print("Selamat Datang di Kuis")
    print("=" * 60)

    nama = input("Masukkan Nama Lengkap: ")
    nim = input("Masukkan NIM: ")
    kategori_soal = input("Masukkan Kategori Soal [DSP/LGA]: ")

    # validasi input
    if kategori_soal.lower() not in ["dsp", "lga"]:
        print("❗ Kategori tidak valid!\n")
    elif not nim.isdigit():
        print("❗ NIM harus berupa angka!\n")
    elif nama.strip() == "" or nim == "":
        print("❗ Nama & NIM tidak boleh kosong!\n")
    else:
        print(f"\nTerpilih Soal {kategori_soal.upper()}. Selamat Mengerjakan, {nama}!\n")
        main()
        break

# submit & revisi jawaban
while True:

    # cari soal yang belum dijawab
    soal_belum_terjawab = [index+1 for index, soal in enumerate(kuis_berdasarkan_kategori) if soal["jawaban"] == ""]

    if soal_belum_terjawab:
        print(f"\n❗ Ada soal yang belum dijawab: {soal_belum_terjawab}")
        pindah_soal = soal_belum_terjawab[0] # otomatis lompat ke soal pertama yg kosong
        print(f"Pindah ke soal {pindah_soal}.\n")

        soal = kuis_berdasarkan_kategori[pindah_soal - 1]

        tampilkan_navigasi()

        print(f"Soal {pindah_soal}")
        print(soal['soal'])
        for key, value in soal['pilihan_jawaban'].items():
            print(f" {key}) {value}")

        # input ulang sampai benar
        while True:
            jawab = input("\nJawaban (a/b/c/d): ").lower().strip()
            if jawab in ['a','b','c','d']:
                soal["jawaban"] = jawab
                print("Jawaban tersimpan.\n")
                break
            else:
                print("Pilih a/b/c/d!")
        continue # kembali cek apakah masih ada soal kosong

    # semua soal terjawab, maka user bisa submit atau revisi
    tampilkan_navigasi()
    submit = input("\nKetik 'submit' untuk kirim atau nomor soal untuk revisi: ").strip().lower()

    # tombol submit
    if submit == "submit":
        skor = hitung_skor(kuis_berdasarkan_kategori)
        tampilkan_hasil(kuis_berdasarkan_kategori, skor)
        break

    # ubah jawaban soal
    elif submit.isdigit():
        nomor = int(submit)
        if 1 <= nomor <= len(kuis_berdasarkan_kategori):

            tampilkan_navigasi()

            soal = kuis_berdasarkan_kategori[nomor - 1]  # ambil soal yg mau direvisi

            print(f"Revisi Jawaban - Soal {nomor}")
            print(soal['soal'])
            for key, value in soal['pilihan_jawaban'].items():
                print(f" {key}) {value}")
            print(f"Jawaban Sebelumnya: {soal['jawaban'].upper()}")

            # input jawaban baru
            while True:
                jawaban_baru = input("\nJawaban baru (a/b/c/d): ").lower().strip()
                if jawaban_baru in ['a','b','c','d']:
                    soal["jawaban"] = jawaban_baru
                    print(f"Jawaban diubah → {jawaban_baru.upper()}\n")
                    break
                else:
                    print("Pilih a/b/c/d!")
        else:
            print("Nomor soal tidak valid!")

    else:
        print("❗ Ketik nomor soal atau 'submit'!")