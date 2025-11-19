import pandas as pd

list_nim=[]
list_nama=[]
list_uts=[]
list_uas=[]
list_total=[]

ulang=5
for i in range(ulang):
    print ("data Ke - " + str(i+1))
    list_nim.append(input("Nim : "))
    list_nama.append(input("Nama : "))
    list_uts.append(int(input("Nilai UTS : ")))
    list_uas.append(int(input("Nilai UAS : ")))

for i in range(ulang):
    list_total.append((list_uas[i] + list_uts[i]) / 2)

tamu = {
    "NIM" : list_nim,
    "Nama Lengkap" : list_nama,
    "Nilai UTS" : list_uts,
    "Nilai UAS" : list_uas,
    "Rata-rata" : list_total
}

data_tamu = pd.DataFrame(tamu)

print("===================== Daftar Nilai =====================")
print(data_tamu)
print("=======================================================")