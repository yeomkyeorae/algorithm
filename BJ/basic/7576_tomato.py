col, row = list(map(int, input().split(' ')))

board = []
tomato = []

all_ripped = True
for r in range(row):
    rows = list(map(int, input().split(' ')))
    
    if rows.count(1) != col:
        all_ripped = False
    
    board.append(rows)
    
    for c, v in enumerate(rows):
        if v == 1:
            tomato.append([r, c])

if all_ripped:
    print(0)
else:
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    time = -1
    while tomato:
        time += 1
        new_tomato = []
        for r, c in tomato:
            for plus_r, plus_c in move:
                new_r = r + plus_r
                new_c = c + plus_c
                if 0 <= new_r < row and 0 <= new_c < col and board[new_r][new_c] == 0:
                    new_tomato.append([new_r, new_c])
                    board[new_r][new_c] = 1
        tomato = new_tomato[:]

    fail = False
    for b in board:
        if 0 in b:
            fail = True
            break
        
    if fail:
        print(-1)
    else:
        print(time)