for letter in "PythonProgramming":
    if letter == "g":
        break
    print(f"Huruf sekarang: {letter}")
print("Good bye!")

print("==="*20)

for letter in "PythonProgramming":
    if letter == "g":
        continue
    print(f"Huruf sekarang: {letter}")
print("Good bye!")