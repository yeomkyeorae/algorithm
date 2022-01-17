S = input()
T = input()


for _ in range(len(T) - len(S)):
    value = T[-1]
    T = T[:len(T) - 1]
    if value == 'B':
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)