ulang = 2

for i in range(ulang):
    print(f"Data Ke - {str(i+1)}")
    nim = input("Masukkan NIM Anda: ")
    uts = int(input("Masukkan Nilai UTS Anda: "))
    uas = int(input("Masukkan Nilai UAS Anda: "))
    print(f"Nim anda adalah %s nilai UTS anda adalah %i dan nilai UAS anda adalah %i" % (nim, uts, uas))
    print("---"*20)