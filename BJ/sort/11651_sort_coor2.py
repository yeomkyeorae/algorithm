n = int(input())

coor_dict = {}
for _ in range(n):
    x, y = map(int, input().split())
    if y in coor_dict.keys():
        coor_dict[y] += [x]
    else:
        coor_dict[y] = [x]

sorted_key = sorted(list(coor_dict))

for key in sorted_key:
    for value in sorted(coor_dict[key]):
        print(value, key)
