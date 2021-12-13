def get_prime_sieves(sieve):
    n = len(sieve)
    
    for i in range(1, n):
        if not sieve[i]: continue
        for j in range(2, n):
            if (i + 1) * j > n: continue
            sieve[(i + 1) * j - 1] = 0
    return sieve


n = int(input())
print()

sieve = [0] * n
for ix, _ in enumerate(sieve):
    sieve[ix] = ix + 1
    
result = get_prime_sieves(sieve)
for p in result:
    if p >= 2:
        print(p)