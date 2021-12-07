from collections import deque
import sys


def solution(N, road, K):
    distance = []
    for _ in range(N):
        distance.append([sys.maxsize] * N)

    road_dict = {}
    for r in road:
        start, end, weight = r
        start -= 1
        end -= 1
        if distance[start][end] > weight:
            distance[start][end] = weight
            distance[end][start] = weight
        
        if start in road_dict.keys():
            road_dict[start].append([end, weight])
        else:
            road_dict[start] = [[end, weight]]

        if end in road_dict.keys():
            road_dict[end].append([start, weight])
        else:
            road_dict[end] = [[start, weight]]

    visited = []
    for _ in range(N):
        visited.append([0] * N)
    
    d = deque()
    d.append(0)
    distance[0][0] = 0
    while d:
        start = d.popleft()
        
        tmp_visited = []
        for end, weight in road_dict[start]:
            if distance[0][end] > distance[0][start] + weight:
                distance[0][end] = distance[0][start] + weight
                
            if visited[start][end]:
                continue

            d.append(end)
            tmp_visited.append([start, end])
            
        for start, end in tmp_visited:
            visited[start][end] = 1

    answer = 0
    for d in distance[0]:
        if d <= K:
            answer += 1
    
    return answer