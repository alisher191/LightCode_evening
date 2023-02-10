"""
a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = [12, 13, 14, 15, 16, 17, 18]
d = 'python'

z = zip(a, b, c, d)
for x in z:
    print(x)
"""

"""
a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = [12, 13, 14, 15, 16, 17, 18]
d = 'python'

z1, z2, z3, z4 = zip(a, b, c, d)
print(z1, z2, z3, z4)

z1, *z2 = zip(a, b, c, d)
print(z1, z2)
"""
"""
a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = [12, 13, 14, 15, 16, 17, 18]
d = 'python'

z = zip(a, b, c, d)
lz = list(z)
print(*lz)
t = tuple(z)
print(t)
"""
