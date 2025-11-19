harga_telur = int(input("Masukkan harga telur (rp): "))
berat_telur = float(input("Masukkan berat telur (kg): "))
ongkos_transport = int(input("Masukkan ongkos transport (rp): "))
uang_ibu = int(input("Masukkan uang ibu (rp): ")) 

total_telur = harga_telur * berat_telur
total_biaya = uang_ibu - (total_telur + ongkos_transport)

if uang_ibu >= (total_telur + ongkos_transport):
    print("Uang ibu cukup")
    print("Sisa uang ibu adalah", total_biaya)
else:
    print("Uang ibu tidak cukup")
    print("Kekurangan uang ibu adalah", abs(total_biaya))