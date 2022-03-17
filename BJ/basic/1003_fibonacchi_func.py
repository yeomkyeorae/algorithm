fibo = [0] * 42
fibo[0] = 0
fibo[1] = 1
fibo[1] = 1

for i in range(39):
    fibo[i + 2] = fibo[i] + fibo[i + 1]

T = int(input())

for _ in range(T):
    N = int(input())
    
    if N == 0:
        print('{} {}'.format(1, 0))
    else:
        print('{} {}'.format(fibo[N - 1], fibo[N]))