def check(row, col):
    if 0 <= row < N and 0 <= col < N:
        return True
    return False


def calc():
    pass


def go(row, col):
    start_r, start_c = row, col
    for a in range(1, N):
        for b in range(1, N):
            for c in range(1, N):
                flag = True
                for d in range(1, N):
                    if flag:
                        for _ in range(a):
                            start_r += direction_map[0][0]
                            start_c += direction_map[0][1]
                        flag = check(start_r, start_c)
                    if flag:
                        for _ in range(b):
                            start_r += direction_map[1][0]
                            start_c += direction_map[1][1]
                        flag = check(start_r, start_c)
                    if flag:
                        for _ in range(c):
                            start_r += direction_map[2][0]
                            start_c += direction_map[2][1]
                        flag = check(start_r, start_c)
                    if flag:
                        for _ in range(d):
                            start_r += direction_map[3][0]
                            start_c += direction_map[3][1]
                        flag = check(start_r, start_c)
                    if flag:
                        calc()


direction_map = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

for row in range(N):
    for col in range(N):
        go(row, col)