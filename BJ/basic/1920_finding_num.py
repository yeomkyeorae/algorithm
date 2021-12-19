n = int(input())
num_list = list(map(int, input().split()))

num_dict = dict()
for num in num_list:
    num_dict[num] = True

m = int(input())
check_list = list(map(int, input().split()))

answer = []
for c in check_list:
    try:
        flag = num_dict[c]
        answer.append(1)
    except Exception:
        answer.append(0)

for a in answer:
    print(a)