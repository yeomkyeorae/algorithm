up, down, height = list(map(int, input().split(' ')))

q, r = divmod((height - up), (up - down))

if r:
    q += 1
q += 1

print(q)