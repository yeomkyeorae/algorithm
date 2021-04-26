def solution(lottos, win_nums):
    lotto_map = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    correct = 0
    not_determined = 0
    for lotto in lottos:
        if lotto in win_nums and lotto != 0:
            correct += 1
        elif lotto == 0:
            not_determined += 1

    best = correct + not_determined
    if best > 6:
        best = 6

    worst = correct

    return [lotto_map[best], lotto_map[worst]]
