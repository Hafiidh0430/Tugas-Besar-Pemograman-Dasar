print("GEROBAK FRIED CHICKEN")
print("----------------------------")
print("Kode\tJenis Potong\tHarga")
print("D\tDada\t\tRp. 2500")
print("P\tPaha\t\tRp. 2000")
print("S\tSayap\t\tRp. 1500")
print("----------------------------")

# daftar menu ayam (disini saya menggunakan dictionary  agar lebih mudah & dinamis)
menu_ayam = [
    {'kode_potong': 'D', 'nama_potong': 'Dada', 'harga_potong': 2500},
    {'kode_potong': 'P', 'nama_potong': 'Paha', 'harga_potong': 2000},
    {'kode_potong': 'S', 'nama_potong': 'Sayap', 'harga_potong': 1500}
]

# inisialisasi variabel lainnya
daftar_pembelian = []
diskon = 0.10  
jumlah_bayar = 0

# loop input berdasarkan banyak jenis dari menu ayam (3 jenis == 3x loop)
for _ in range(len(menu_ayam)):
    # input untuk memasukkan kode potong
    kode_input = input("Kode Potong [D/P/S]: ").upper()

    # next(), untuk mencari data menu yang sesuai dengan kode_input
    data_menu = next(
        (data for data in menu_ayam if data['kode_potong'] == kode_input),
        None  # kalau tidak ditemukan, hasilnya None
    )

    # jika data menunya tidak sesuai dengan input kode, maka print pesan error
    if data_menu is None:
        print("Kode tidak ditemukan. Silakan coba lagi.")
        # lanjut ke iterasi berikutnya sampai input yang benar
        continue

    # hitung banyak potong dan total harga
    banyak_potong = int(input("Banyak Potong: "))
    total_harga = data_menu['harga_potong'] * banyak_potong

    # insert data pembelian ke array daftar_pembelian
    daftar_pembelian.append({
        'nama_potong': data_menu['nama_potong'],
        'harga_potong': data_menu['harga_potong'],
        'jumlah_beli': banyak_potong,
        'total_harga': total_harga
    })

# tampilkan hasil akhir
print("\nGEROBAK FRIED CHICKEN")
print("-------------------------------------------------------------")
print("No\tJenis Potong\tHarga Satuan\tJumlah Beli\tTotal Harga")
print("-------------------------------------------------------------")

# loop untuk menampilkan daftar pembelian
for nomor, pembelian in enumerate(daftar_pembelian, start=1):
    print(
        f"{nomor}\t{pembelian['nama_potong']}\t\tRp.{pembelian['harga_potong']}\t\t"
        f"{pembelian['jumlah_beli']}\t\tRp.{pembelian['total_harga']}"
    )   
    jumlah_bayar += pembelian['total_harga']

# hitung pajak dan total bayar
pajak = jumlah_bayar * diskon
total_bayar = jumlah_bayar + pajak

print("-------------------------------------------------------------")
print(f"Jumlah Bayar: Rp. {jumlah_bayar}")
print(f"Pajak 10%: Rp. {int(pajak)}")
print(f"Total Bayar: Rp. {int(total_bayar)}")