tries = int(input())

for t in range(1, tries + 1):
    N = int(input())
    string = str(N)
    num = int(string[-1])
    if num % 2:
        answer = 'Odd'
    else:
        answer = 'Even'

    print('#{} {}'.format(t, answer))
