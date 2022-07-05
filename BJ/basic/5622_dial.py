string = input()

d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

answer = 0
for ch in string:
    for ix, group in enumerate(d):
        if ch in group:
            answer += ix + 3

print(answer)
