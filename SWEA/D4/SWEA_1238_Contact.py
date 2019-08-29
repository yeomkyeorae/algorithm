from collections import deque


def bfs(start):

    queue = deque()
    queue.append([start, 0])
    to_return = []

    while len(queue) > 0:
        popped = queue.popleft()
        visited[popped[0] - 1] = 1
        flag = True
        for one_tuple in to_return:
            if one_tuple[0] == popped[0]:
                flag = False
                break
        if flag:
            to_return.append(popped)

        if popped[0] in graph_dict.keys():
            for to in graph_dict[popped[0]]:
                if visited[to - 1] == 0:
                    queue.append([to, popped[1] + 1])

    return to_return


for t in range(1, 11):
    _, start = map(int, input().split())

    input_list = list(map(int, input().split()))

    graph_dict = {}
    for i in range(0, len(input_list), 2):
        if input_list[i] in graph_dict.keys():
            graph_dict[input_list[i]].append(input_list[i + 1])
        else:
            graph_dict[input_list[i]] = [input_list[i + 1]]

    visited = [0] * 100
    result = bfs(start)

    tmp_list = []
    max_value = -1
    for tup in result:
        if tup[1] > max_value:
            max_value = tup[1]

    for tup in result:
        if tup[1] == max_value:
            tmp_list.append(tup[0])

    print('#{} {}'.format(t, max(tmp_list)))

