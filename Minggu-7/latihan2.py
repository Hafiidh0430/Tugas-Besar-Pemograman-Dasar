mat1 = [
    [9, 0],
    [3, 6]
]

mat2 = [
    [6, 0],
    [7, 2]
]

# penjumlahan matriks
for x in range(len(mat1)):
    for y in range(len(mat1[0])):
        print(mat1[x][y] + mat2[x][y], end=" ")
    print()
    
# pengurangan matriks
for x in range(len(mat1)):
    for y in range(len(mat1[0])):
        print(mat1[x][y] - mat2[x][y], end=" ")
    print()