import heapq


def solution(scoville, K):
    h = []
    for s in scoville:
        heapq.heappush(h, s)
    if not len(h) > 1:
        return -1
    answer = 0
    while True:
        for i in range(2):
            if i == 0:
                first = heapq.heappop(h)
                if first >= K:
                    return answer
            else:
                second = heapq.heappop(h)
                if second == 0:
                    return -1
        new = first + second * 2
        heapq.heappush(h, new)
        if len(h) == 1:
            if h[0] < K:
                return -1
        answer += 1