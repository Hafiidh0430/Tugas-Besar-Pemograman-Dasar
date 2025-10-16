# data karyawan
kontrak_karyawan = 300000
jam_kerja = 8
honor_lembur = 3500

# variabel global
tunjangan_jabatan, tunjangan_pendidikan, total_gaji, total_lembur = 0, 0, 0, 0

# data jabatan
data_jabatan = [
    {"golongan": 1, "tunjangan": 0.05}, 
    {"golongan": 2, "tunjangan": 0.1}, 
    {"golongan": 3, "tunjangan": 0.15}
]

# data pendidikan
data_pendidikan = [
    {"pendidikan": "SMA", "persentase": 0.025}, 
    {"pendidikan": "D1", "persentase": 0.05}, 
    {"pendidikan": "D3", "persentase": 0.2},
    {"pendidikan": "S1", "persentase": 0.3}
]

# input data karyawan
nama_karyawan = input("Nama Karyawan: ")
golongan_jabatan = int(input("Golongan Jabatan [1/2/3]: "))
golongan_pendidikan = input("Pendidikan [SMA/D1/D3/S1]: ")
jumlah_jam_kerja = int(input("Jumlah Jam Kerja: "))

# loop untuk mencari data jabatan
for jabatan in data_jabatan:
     # mencari data yang sesuai dengan input jabatan
    if golongan_jabatan == jabatan["golongan"]:
        # hitung tunjangan jabatan
        tunjangan_jabatan = kontrak_karyawan * jabatan["tunjangan"]
        break

# loop untuk mencari data pendidiakn
for pendidikan in data_pendidikan:
    # mencari data yang sesuai dengan input pendidikan
    if golongan_pendidikan.lower() == pendidikan["pendidikan"].lower():
        # hitung tunjangan pendidikan
        tunjangan_pendidikan = kontrak_karyawan * pendidikan["persentase"]
        break   

# hitung total lenbur jika melebihi jam kerja (8 jam)
if jumlah_jam_kerja > jam_kerja:
    # hitung total lembur
    total_lembur = (jumlah_jam_kerja - jam_kerja) * honor_lembur

# hitung total gaji
total_gaji = sum([kontrak_karyawan, tunjangan_jabatan, tunjangan_pendidikan, total_lembur])

# print hasil
print("-----------------------------")
print(f"Nama Karyawan: {nama_karyawan}")
print(f"Honor Yang Diterima:")
print(f"-> Tunjangan Jabatan: Rp. {tunjangan_jabatan}")
print(f"-> Tunjangan Pendidikan: Rp. {tunjangan_pendidikan}")
print(f"-> Honor Lembur: Rp. {total_lembur}")
print("-----------------------------")
print(f"Total Gaji: Rp. {total_gaji}")
print("-----------------------------")