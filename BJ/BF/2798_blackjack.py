def comb(k, start):
    global card_comb

    if k == 3:
        card_comb.append(choose.copy())
        return

    for i in range(start, len(cards)):
        choose.append(cards[i])
        comb(k + 1, i + 1)
        choose.pop()


n, m = map(int, input().split())
cards = list(map(int, input().split()))

card_comb = []
choose = []
comb(0, 0)
max_value = 0
for one_list in card_comb:
    sum_value = sum(one_list)
    if max_value < sum_value <= m:
        max_value = sum_value

print(max_value)
