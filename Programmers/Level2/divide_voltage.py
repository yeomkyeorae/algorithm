from collections import deque


def go(ways, start_key, ban_key, ban_value, n):
    d = deque()
    d.append(start_key)
    
    visited = []
    for _ in range(n + 1):
        visited.append([0] * (n + 1))
    
    cnt = 1
    while d:
        key = d.popleft()
        if key in ways.keys():
            for value in ways[key]:
                if (key == ban_key and value == ban_value) or (key == ban_value and value == ban_key):
                    continue
                if visited[key][value] or visited[value][key]:
                    continue
                visited[key][value] = 1
                visited[value][key] = 1
                
                d.append(value)
                cnt += 1
    return cnt     


def solution(n, wires):
    ways = dict()
    for w in wires:
        if w[0] in ways.keys():
            ways[w[0]].append(w[1])
        else:
            ways[w[0]] = [w[1]]
        if w[1] in ways.keys():
            ways[w[1]].append(w[0])
        else:
            ways[w[1]] = [w[0]]
    
    answer = 10000
    for w in wires:
        ban_key, ban_value = w
        start_key = wires[0][0]
        
        num = go(ways, start_key, ban_key, ban_value, n)
        abs_value = abs((n - num) - num)
        if abs_value < answer:
            answer = abs_value

    return answer