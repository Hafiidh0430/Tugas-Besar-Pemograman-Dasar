from fractions import Fraction as F

# output: 2/3
print(F(1,3) + F(1,3))

# output: 6/5
print(1 / F(5,6))

# output true
print(F(-3, 10) < 3)