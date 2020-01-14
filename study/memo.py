a = [(3, 1), (2, 1), (1, 1)]

a.sort(key=lambda x: x[0])
a.sort(key=lambda x: x[1])

print(a)