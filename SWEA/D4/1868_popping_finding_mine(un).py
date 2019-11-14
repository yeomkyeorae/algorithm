# from collections import deque
#
#
# directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
# def transfer(row, col):
#     d = deque()
#     d.append([row, col])
#     visited = board
#     visited[row][col] = 'v'
#     while d:
#         popped = d.popleft()
#         flag = True
#         tmp_directions = []
#         for direction in directions:
#             new_row = popped[0] + direction[0]
#             new_col = popped[1] + direction[1]
#             if 0 <= new_row < n and 0 <= new_col < n:
#                 if board[new_row][new_col] == '*':
#                     flag = False
#                     break
#                 elif board[new_row][new_col] == '.':
#                     tmp_directions.append([new_row, new_col])
#         if flag:
#             for direction in tmp_directions:
#                 d.append([direction[0], direction[1]])
#                 visited[direction[0]][direction[1]] = 'v'
#         else:
#             tmp_directions.clear()
#     return visited
#
#
# def go(row, col, stage):
#     global answer
#
#     if answer < stage:
#         return
#     tmp_dots = []
#     for r in range(n):
#         for c in range(n):
#             if board[r][c] == '.':
#                 tmp_dots.append([r, c])
#
#     visited = transfer(row, col)
#
#     tmp_dots2 = []
#     for dot in tmp_dots:
#         if visited[dot[0]][dot[1]] == 'v':
#             tmp_dots2.append([dot[0], dot[1]])
#
#     flag = True
#     for y in range(n):
#         for x in range(n):
#             if board[y][x] == '.':
#                 flag = False
#                 break
#         if not flag:
#             break
#     if flag:
#         if stage < answer:
#             answer = stage
#         return
#
#     for row in range(n):
#         for col in range(n):
#             if board[row][col] == '.':
#                 go(row, col, stage + 1)
#                 for dot in tmp_dots2:
#                     board[dot[0]][dot[1]] = '.'
#
#
# tries = int(input())
#
# for t in range(1, tries + 1):
#     n = int(input())
#
#     board = []
#     for _ in range(n):
#         chars = input()
#         tmp = []
#         for ch in chars:
#             tmp.append(ch)
#         board.append(tmp)
#
#     answer = 100000
#     for row in range(n):
#         for col in range(n):
#             if board[row][col] == '.':
#                 go(row, col, 1)
#
#     print('#{} {}'.format(t, answer))
