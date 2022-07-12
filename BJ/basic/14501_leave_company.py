max_value = 0


def go(board, max_stay, loc, score):
    global max_value

    if max_stay < loc:
        return

    if score > max_value:
        max_value = score

    for ix in range(loc, len(board)):
        t, p = board[ix]
        score += p
        go(board, max_stay, ix + t, score)
        score -= p


num = int(input())

board = []
for _ in range(num):
    num_list = list(map(int, input().split()))
    board.append(num_list)

for ix, el in enumerate(board):
    t, p = el
    go(board, num, ix + t, p)

print(max_value)
