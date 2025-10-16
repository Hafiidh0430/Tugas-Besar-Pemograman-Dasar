harga_telur = int(input("Masukkan harga telur (rp): "))
berat_telur = float(input("Masukkan berat telur (kg): "))
uang_ibu = int(input("Masukkan uang ibu (rp): "))

total_telur = harga_telur * berat_telur
total_biaya = uang_ibu - total_telur

print("Total harga adalah", total_telur)
print("Kembalian adalah", abs(total_biaya))