import heapq
import sys


INF = sys.maxsize
graph = [
    [0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0]
]
N = 6        
    

def dijkstra(start):  
    # 초기화  
    # distances: start에서 각 노드들로 이동할 수 있는 최단 거리
    distances = [INF] * N
    distances[start] = 0
    
    queue = []
    # 배열 또는 튜플 형태로 heapq에 삽입할 경우 첫 번째 요소를 기준으로 정렬
    # heapq에 의해 방문해야할 노드 중 최단 거리를 바로 알 수 있음
    heapq.heappush(queue, [distances[start], start])
    
    # start에서 방문한 노드 모음(queue에 삽입된 것들): A
    while queue:
        # 현재 방문해야할 최단 거리 노드
        # current_destination: B
        current_distance, current_destination = heapq.heappop(queue)
        
        # 기존 거리보다 멀면 고려하지 않음
        if distances[current_destination] < current_distance:
            continue
        
        # new_detination: C
        # B에서 갈 수 있는 C
        for new_destination, new_distance in enumerate(graph[current_destination]):
            distance = current_distance + new_distance
            
            # (A -> B -> C) < (A -> C)
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
                              
    return distances
        

dijkstra(0)