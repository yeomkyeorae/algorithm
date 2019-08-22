from collections import deque

result = []

def dfs(dic, stack, start, did_you_go, result):


    if did_you_go[start - 1] == 1:
        return result

    did_you_go[start - 1] = 1
    result.append(str(start))

    for value in dic[start]:
        if did_you_go[value - 1] == 0:
            result = dfs(dic, stack, value, did_you_go, result)


def bfs(dic, queue, did_you_go, result):

    while len(queue) > 0:
        key = queue.popleft()
        did_you_go[key - 1] = 1
        for value in dic[key]:
            if did_you_go[value - 1] == 1:
                continue
            elif value not in queue:
                queue.append(value)
        result.append(str(key))

    return result


if __name__ == '__main__':
    vertex, edge, start = map(int, input().split())

    edge_dict = {k: [] for k in range(1, vertex + 1)}
    tmp_list = []
    for _ in range(edge):
        a, b = map(int, input().split())
        tmp_list.append((a, b))

    tmp_list.sort(key=lambda x: x[1])

    for a, b in tmp_list:
        edge_dict[a].append(b)
        edge_dict[b].append(a)

    # dfs
    stack = []
    did_you_go = [0] * vertex
    result1 = dfs(edge_dict, stack, start, did_you_go, [])
    print(' '.join(result1))

    # bfs
    queue = deque()
    queue.append(start)
    did_you_go = [0] * vertex
    result2 = bfs(edge_dict, queue, did_you_go, [])
    print(' '.join(result2))
