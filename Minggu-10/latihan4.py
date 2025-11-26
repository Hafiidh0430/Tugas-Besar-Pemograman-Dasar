import sys

list = ['a', 0, 4]
for each in list:
    try:
        print(f"Masukkan: {each}")
        r = 1/int(each)
        break
    except:
        print(f"Upps! {sys.exc_info()[0]} terjadi.")
        print("Masukkan berikutnya.")
        print()
print(f"Kebalikan dari {each} = {r}")