def comb(k, start):

    global store_comb

    if k == R:
        store_comb.append(choose.copy())
        return

    for i in range(start, N):
        choose.append(chicken[i])
        comb(k + 1, i + 1)
        choose.pop()


n, m = map(int, input().split())

house = []
chicken = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j, value in enumerate(tmp):
        if value == 2:
            chicken.append((i, j))
        elif value == 1:
            house.append((i, j))

all_dist = []
for c in chicken:
    for h in house:
        all_dist.append([(c[0], c[1]), (h[0], h[1]), abs(c[0] - h[0]) + abs(c[1] - h[1])])

N = len(chicken)
R = m
choose = []
store_comb = []

if R == N:
    store_comb = [chicken]
else:
    comb(0, 0)

MIN_VALUE = 100000
for one_comb in store_comb:  # 고를 수 있는 치킨가게 조합 하나씩
    house_dict = {}
    for one_dist in all_dist:  # 집과 치킨가게 사이의 모든 조합 하나씩
        if one_dist[0] in one_comb:  # 거리를 구한 치킨가게가 조합 중에 있으면
            if not one_dist[1] in house_dict.keys():  # 아직 dict에 해당 집이 없으면
                house_dict[one_dist[1]] = one_dist[2]
            else:                                     # 더 가까운 가게로 갱신
                if house_dict[one_dist[1]] > one_dist[2]:
                    house_dict[one_dist[1]] = one_dist[2]

    tmp = 0
    for value in house_dict.values():
        tmp += value
    if tmp < MIN_VALUE:
        MIN_VALUE = tmp

print(MIN_VALUE)
