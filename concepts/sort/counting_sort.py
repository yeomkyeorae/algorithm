arr = [0, 4, 1, 3, 1, 2, 4, 1]
# 양의 정수, 최댓값을 알아야 한다.
# 최댓값 = 4
cnt = [0] * 5  # 배열의 인덱스 n - 1 = 4

# 빈도 수 계산
for val in arr:
    cnt[val] += 1

# 누적 빈도 수 계산
for i in range(1, len(cnt)):
    cnt[i] = cnt[i-1] + cnt[i]

result = [0] * len(arr)
for ix in range(len(arr)-1, -1, -1):
    cnt[arr[ix]] -= 1
    result[cnt[arr[ix]]] = arr[ix]
print(result)
