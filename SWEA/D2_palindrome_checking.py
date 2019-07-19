tries = int(input())
for one_try in range(1, tries + 1):
    string = input()
    print('#{} {}'.format(one_try, 1)) if string == ''.join([ch for ch in string[::-1]]) else print('#{} {}'.format(one_try, 0))
