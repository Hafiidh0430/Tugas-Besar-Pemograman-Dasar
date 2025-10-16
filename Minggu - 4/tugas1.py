# data tiket bus
data_tiket = [
    {"kode_jurusan": "SBY", "nama_kota": "Surabaya", "harga_tiket": 300000},
    {"kode_jurusan": "BL", "nama_kota": "Bali", "harga_tiket": 350000},
    {"kode_jurusan": "LMP", "nama_kota": "Lampung", "harga_tiket": 500000},
]

# global variables
nama_kota, harga_tiket, total_harga, potongan_harga, uang_kembali = "", 0, 0, 0, 0
jumlah_tiket, uang_bayar = 0, 0

# input data pembeli
nama_pembeli = input("Nama Pembeli: ")
no_hp = input("Nomor HP Pembeli: ")
jurusan = input("Kode Jurusan [SBY/BL/LMP]: ")

# loop for all data tiket
for tiket in data_tiket:
    
    # find matching kode jurusan by input jurusan
    if jurusan.lower() == tiket["kode_jurusan"].lower():
        
        # show ticket details
        print("-----------------------------")
        
        nama_kota = tiket["nama_kota"]
        harga_tiket = tiket["harga_tiket"]
        
        print(f"Kode Jurusan: {tiket['kode_jurusan']}")
        print(f"Nama Kota Tujuan: {tiket['nama_kota']}")
        print(f"Harga Tiket: Rp. {tiket['harga_tiket']}")
        
        print("-----------------------------")
        
        # next for input jumlah tiket and uang bayar
        jumlah_tiket = int(input("Jumlah Tiket Yang Dibeli: "))
        uang_bayar = int(input("Jumlah Uang Yang Dibayar: "))
        
        # calculate potongan harga, if ticket >= 3 get 10% offer
        if jumlah_tiket >= 3:
            potongan_harga = tiket["harga_tiket"] * 10/100
            
        # calclulate total harga and uang kembali
        total_harga = (jumlah_tiket * tiket["harga_tiket"]) - potongan_harga
        uang_kembali = uang_bayar - total_harga
        
        # print all details
        print("-----------------------------")
        print("Penjualan Tiket Bus XYZ")
        print("-----------------------------")
        print(f"Nama Pembeli: {nama_pembeli}")
        print(f"No. HP: {no_hp}")
        print(f"Kode Jurusan: {jurusan}")
        print(f"Nama Kota Tujuan: {nama_kota}")
        print(f"Harga Tiket: Rp. {harga_tiket}")
        print(f"Jumlah Tiket: {jumlah_tiket}")
        print("-----------------------------")
        print(f"Potongan: {potongan_harga}")
        print(f"Total Bayar: {total_harga}")
        print(f"Uang Bayar: {uang_bayar}")
        print(f"Uang Kembali: {uang_kembali}")
        break
    
# forelse if no matching kode jurusan found
else:
    # if kode jurusan not found
    print("Kode jurusan tidak ditemukan")
        

    
