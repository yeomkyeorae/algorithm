def solution(brown, yellow):
    width, height = 0, 0

    for y in range(0, yellow):
        q = y + 1
        if yellow % q == 0:
            p = yellow // q
            if (p * 2) + (q * 2) + 4 == brown:
                if p <= q:
                    width, height = q, p
                else:
                    width, height = p, q
                break

    return [width + 2, height + 2]
