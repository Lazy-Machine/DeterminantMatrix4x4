from itertools import permutations as permute
from sympy.combinatorics import Permutation as perm

n = int(input('NxN= '))
m = []
p = list(permute(range(n)))
det = 0

for i in range(n):
    row = []
    for j in range(n):
        val = int(input(f"L{i+1},C{j+1}: "))
        row.append(val)
    m.append(row)

for l in m:
    print ('  '.join(map(str, l)))

for pi in p:
    sgn = perm(pi).signature()
    product = 1
    for i in range(n):
        product *= m[i][pi[i]]
    det += sgn * product

print("Det=", det)