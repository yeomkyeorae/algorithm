def possible(k, i):     # k: 행, i : 열
    for j in range(k):  # j번 퀸의 위치(j, arr[j])
        if k - j == abs(i - arr[j]):
            return False

    return True


def go(k, n):   # k : 행

    global count

    if k == n:
        count += 1
        return

    for i in range(n):  # i : 열
        if visited[i]:
            continue
        if not possible(k, i):
            continue
        visited[i] = 1
        arr[k] = i
        go(k + 1, n)
        visited[i] = 0


n = int(input())

arr = [0] * n
visited = [0] * n
flag = False
count = 0
go(0, n)
print(count)
