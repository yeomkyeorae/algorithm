board = []
answer = 1000000
width = 50 * 2 + 1
visited = []
end_row = None
end_col = None


def go(start_row, start_col, length):
    global board
    global answer
    global width
    global visited
    global end_row
    global end_col
    
    if board[start_row][start_col] != 1:
        return

    if start_row == end_row and start_col == end_col:
        if answer > length:
            answer = length
        return
    
    visited[start_row][start_col] = 1
    
    for move in [-1, 1]:
        if 0 <= start_row + move < width:
            if not visited[start_row + move][start_col]:
                go(start_row + move, start_col, length + 1)
        if 0 <= start_col + move < width:
            if not visited[start_row][start_col + move]:
                go(start_row, start_col + move, length + 1)
                
                
def solution(rectangle, characterX, characterY, itemX, itemY):
    global board
    global answer
    global width
    global visited
    global end_row
    global end_col
    
    c_x = characterX * 2 - 1
    c_y = width - characterY * 2 - 1
    end_col = itemX * 2 - 1
    end_row = width - itemY * 2 - 1
    
    for _ in range(width):
        board.append([0] * width)
        visited.append([0] * width)
    
    outer = set()
    inner = set()
    for rect in rectangle:
        col1, row1, col2, row2 = rect
        col1 = col1 * 2 - 1
        col2 = col2 * 2 - 1
        row1 = width - row1 * 2 - 1
        row2 = width - row2 * 2 - 1
        for r in range(row1 - row2 + 1):
            for c in range(col2 - col1 + 1):
                if r == 0 or r == row1 - row2 or c == 0 or c == col2 - col1:
                    if not (r + row2, c + col1) in inner:
                        outer.add((r + row2, c + col1))
                else:
                    inner.add((r + row2, c + col1))
                    tmp_set = set()
                    tmp_set.add((r + row2, c + col1))
                    outer = outer.difference(tmp_set)
                    
    for r, c in list(outer):
        board[r][c] = 1

    go(c_y, c_x, 0)
    
    return answer // 2