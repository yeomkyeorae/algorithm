from itertools import product, permutations

ix = 0
for i in product([1,2,3,4], repeat=4):
    ix += 1
print(ix)

ix = 0
for i in permutations([0, 1, 2, 3, 4]):
    print(i)
    ix += 1
print(ix)