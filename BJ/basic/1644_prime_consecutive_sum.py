N = int(input())

nums = [1] * (N + 1)
nums[0] = 0
nums[1] = 0

primes = []
for i in range(2, N + 1):
    if nums[i]:
        primes.append(i)
        for j in range(2 * i, N + 1, i):
            nums[j] = 0

answer = 0
for i in range(len(primes)):
    for j in range(i + 1, len(primes) + 1):
        sum_value = sum(primes[i:j])
        
        if sum_value == N:
            answer += 1
            break
        elif sum_value > N:
            break

print(answer)
