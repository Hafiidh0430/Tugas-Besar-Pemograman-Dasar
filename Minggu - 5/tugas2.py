print("===== No.1 =====")
for i in range(1, 11):
    print(i, end=", ")
    
print("\n===== No.2 =====")
for i in range(10, 0, -1):
    print(i, end=", ")
    
print("\n===== No.3 =====")
for i in range(3, 21, 3):
    print(i, end=", ")

print("\n===== No.4 =====")
for i in range(4, 21, 4):
    print(i, end=", ")
    
print("\n===== No.5 =====")
a, b = 0, 1
for i in range(10):
    print(b, end=", ")
    a, b = b, a + b
      