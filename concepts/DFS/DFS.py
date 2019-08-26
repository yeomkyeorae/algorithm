import sys
sys.stdin = open('DFS_input.txt', 'r')

# 반복문
def DFS_iter(v):
    # 시작점을 방문하고, 스택에 push
    stack = []
    visit[v] = True; print(v, end=' ')
    stack.append(v)

    while stack:    # 빈 스택이 아닐 동안 반복
        for w in graph[v]:
            if not visit[w]:
                visit[w] = True; print(w, end=' ')
                stack.append(v)
                v = w
                break
        else:
            v = stack.pop()


# 재귀
def DFS_self(v):
    visit[v] = True; print(v, end=' ')

    for w in graph[v]:
        if not visit[w]:
            DFS_self(w)


vertex, edge = map(int, input().split())   # 정점 수, 간선 수
graph = [[] for _ in range(vertex + 1)]     # 1 ~ V까지
visit = [False] * (vertex + 1)          # 방문 정보

for _ in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

DFS_self(1)
# DFS_iter(1)

