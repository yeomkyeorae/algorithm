class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))
        
        q = [[0, k]]
        
        dist = collections.defaultdict(int)
        
        # 우선순위 큐의 최솟값을 기준으로 정점까지의 최단 경로를 삽입
        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(q, (alt, v))
                    
        if len(dist) == n:
            return max(dist.values())
        
        return -1
        