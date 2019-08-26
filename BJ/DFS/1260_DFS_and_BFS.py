from collections import deque


def dfs(start, edge_dict):
    global result
    global visited

    if visited[start - 1] == 1:
        return

    visited[start - 1] = 1
    result.append(str(start))

    for edge in edge_dict[start]:
        if visited[edge - 1] == 0:
            dfs(edge, edge_dict)


def bfs(start, edge_dict):
    global result
    global visited

    queue = deque()
    queue.append(start)
    visited[start - 1] = 1

    while len(queue) > 0:
        start = queue.popleft()
        result.append(str(start))

        for edge in edge_dict[start]:
            if visited[edge - 1] == 0:
                queue.append(edge)
                visited[edge - 1] = 1


if __name__ == '__main__':
    vertex, edge, start = map(int, input().split())

    edge_dict = {k: [] for k in range(1 , vertex + 1)}
    for _ in range(edge):
        a, b = map(int, input().split())
        edge_dict[a].append(b)
        edge_dict[b].append(a)

    for key in edge_dict.keys():
        edge_dict[key].sort()

    # dfs
    result = []
    visited = [0] * vertex
    dfs(start, edge_dict)
    print(' '.join(result))

    # bfs
    result = []
    visited = [0] * vertex
    bfs(start, edge_dict)
    print(' '.join(result))
