# Longest Increasing Subsooyeol
# 수열 중에서 가장 길게 증가하는 부분 순열 찾기

n = int(input())
nums = list(map(int, input().split()))

d = [0] * n
v = [0] * n     # 어느 index의 값을 더했는지 기록
for ix, num in enumerate(nums):
    d[ix] = 1
    max_index = -1
    max_value = 0
    v[ix] = ix
    for j in range(ix - 1, -1, -1):
        if nums[j] < nums[ix]:
            if d[j] > max_value:
                max_value = d[j]
                max_index = j
                v[ix] = j
    d[ix] = d[ix] + max_value

MAX = max(d)
print(MAX)

# v에 저장된 index를 기반으로 부분 수열 찾기
# MAX 값 저장된 index
d_i = d.index(MAX)
# MAX 값은 어느 index의 값과 더했나
v_i = v[d_i]
# v_v_list: 순열 값
v_v_list = [nums[d_i]]
# index 따라서 순열 값 저장
while len(v_v_list) < MAX:
    v_v_list.append(nums[v_i])
    v_i = v[v_i]
v_v_list.sort()
for a in v_v_list:
    print(a, end=' ')
