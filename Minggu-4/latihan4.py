kode_baju = input("Masukkan kode baju [SP/AD]:")
ukuran = input("Masukkan ukuran baju [S/M]:")

if kode_baju == "SP" or kode_baju == "sp":
    merk = "SuperDry"
    if ukuran == "S" or ukuran == "s":
        harga = 450000
    elif ukuran == "M" or ukuran == "m":
        harga = 500000
    else:
        harga = 0
elif kode_baju == "AD" or kode_baju == "ad":
    merk = "Adidas"
    if ukuran == "S" or ukuran == "s":
        harga = 650000
    elif ukuran == "M" or ukuran == "m":
        harga = 700000
    else:
        harga = 0
else:
    merk = "Anda Salah Input Kode Merk"
    harga = 0
    
print("-----------------------------")
print(f"Merk Baju: {str(merk)}")
print(f"Harga Baju: Rp. {harga}")