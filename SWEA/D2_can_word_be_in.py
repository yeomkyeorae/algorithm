tries = int(input())

for i in range(1, tries + 1):
    n, k = map(int, input().split())
    board = []

    for _ in range(n):
        board.append(list(map(int, input().split())))

    print(board)
