tries = int(input())

for i in range(1, tries + 1):
    num = int(input())

    prime_dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}

    while num > 1:
        if num % 2 == 0:
            num /= 2
            prime_dict[2] = prime_dict[2] + 1
        elif num % 3 == 0:
            num /= 3
            prime_dict[3] = prime_dict[3] + 1
        elif num % 5 == 0:
            num /= 5
            prime_dict[5] = prime_dict[5] + 1
        elif num % 7 == 0:
            num /= 7
            prime_dict[7] = prime_dict[7] + 1
        elif num % 11 == 0:
            num /= 11
            prime_dict[11] = prime_dict[11] + 1

    prime_dict = {k: str(v) for k, v in prime_dict.items()}

    print('#{} {}'.format(i, ' '.join(prime_dict.values())))
