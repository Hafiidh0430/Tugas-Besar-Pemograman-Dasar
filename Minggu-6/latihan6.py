# add single value to list
ganjil = [1, 3, 5, 7]
ganjil.append(9)
print(ganjil)

# add multiple values to list
ganjil.extend([11, 13, 15])
print(ganjil)

# add using "+"
genap = [2, 4, 6]
print(genap + [8, 10, 12])
print(["p", "y"] * 2)

# using insert
ganjil = [5, 7, 11, 13, 15]
ganjil.insert(0, 3) # insert 3 at index 0
print(ganjil)

# remove list 
my_list = ["p", "y", "t", "h", "o", "n", "i", "n", "d", "o"]
my_list.remove("n") # just remove the first one of words
print(my_list)

# remove using "pop()"
print(my_list.pop(1)) # return the removed value

# using "del"
del my_list[2]
print(my_list)

# clear all
my_list.clear()
print(my_list)

