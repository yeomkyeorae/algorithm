def solution(citations):
    answer = 0
    citations.sort()
    for ix, d in enumerate(citations):
        for h in range(1, d + 1):
            if h <= len(citations[ix:]):
                if h >= len(citations[:ix]):
                    if h > answer:
                        answer = h
            
    return answer

# 시간이 오래 걸린다
# 아마 두 번째 for에서 h가 가질 수 있는 범위가 너무 커서 그런 것 같다.