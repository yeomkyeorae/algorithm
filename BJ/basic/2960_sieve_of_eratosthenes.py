def get_prime_sieves(sieve, k):
    n = len(sieve)
    
    deleted = []
    for i in range(1, n):
        if not sieve[i]: continue
        for j in range(1, n):
            if (i + 1) * j > n: continue
            if not sieve[(i + 1) * j - 1]: continue
            
            deleted.append((i + 1) * j)
            if len(deleted) == k:
                return (i + 1) * j
            
            sieve[(i + 1) * j - 1] = 0
    return sieve


n, k = map(int, input().split())

sieve = [0] * n
for ix, _ in enumerate(sieve):
    sieve[ix] = ix + 1
    
result = get_prime_sieves(sieve, k)
print(result)