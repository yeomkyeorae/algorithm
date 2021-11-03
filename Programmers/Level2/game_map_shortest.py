from collections import deque


def solution(maps):
    answer = 0
    visited = []
    
    end_row = len(maps)
    end_col = len(maps[0])
    for _ in maps:
        visited.append([0] * end_col)
    
    d = deque()
    row, col = 0, 0
    visited[row][col] = 1
    distance = 1
    d.append([row, col, distance])
    while d:
        row, col, distance = d.popleft()
        
        flag = False
        for r in [-1, 1]:
            if 0 <= row + r < end_row and not visited[row + r][col] and maps[row + r][col]:
                visited[row + r][col] = 1
                d.append([row + r, col, distance + 1])
                flag = True
        
        for c in [-1, 1]:
            if 0 <= col + c < end_col and not visited[row][col + c] and maps[row][col + c]:
                visited[row][col + c] = 1
                d.append([row, col + c, distance + 1])
                flag = True

        if visited[end_row - 1][end_col - 1]:
            answer = distance + 1
            break
    
    if not d:
        answer = -1
    
    return answer