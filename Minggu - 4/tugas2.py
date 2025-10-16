# empty array as data kuliah
data = []

# input data kuliah
nis = input("NIS Mahasiswa: ")
nama = input("Nama: ")
jurusan = input("Jurusan [SI/SIA]: ")

# while loop condition for repeat input data
ulangi_pengisian = True

# loop for adding data to empty array as long as user want to repeat input data
while ulangi_pengisian:
    
    # append data to array with detail of data kuliah inputs
    data.append({
        "nis": nis,
        "nama": nama,
        "jurusan": (
            "Sistem Informasi" if jurusan == "SI"
            else "Sistem Informasi Akutansi" if jurusan == "SIA"
            else jurusan
        )
    })
    
    # ask user if they want to repeat input data
    ulangi = input("Apakah anda ingin mengisi data lagi? [y/t]: ")
    
    # if yes, then repeat it
    if ulangi.lower() == 'y':
        
        # input data kuliah again
       nis = input("NIS Mahasiswa: ")
       nama = input("Nama: ")
       jurusan = input("Jurusan [SI/SIA]: ")
        
    # if no, then change ulangi_pengisian to false to stop the loop
    else:
        ulangi_pengisian = False

# print all data kuliah in tabular format
print(f"{'NIS':<15}{'Nama Mahasiswa':<20}{'Jurusan':>10}")
print("-" * 45)
for item in data:
    print(f"{item['nis']:<15}{item['nama']:<20}{item['jurusan']:>10}")