N, M = list(map(int, input().split()))

sieze = [1] * (M + 1)
sieze[0] = 0
sieze[1] = 0
for num in range(2, len(sieze)):
    if not sieze[num]:
        continue
    
    current = num * 2
    while current < len(sieze):
        sieze[current] = 0
        current += num

for ix, num in enumerate(sieze[N:M + 1]):
    if num:
        print(ix + N)