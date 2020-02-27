def solution(N, stages):
    current_dict = {}
    current_key = []
    for s in stages:
        if s == N + 1:
            continue
        if s in current_dict.keys():
            current_dict[s] += 1
        else:
            current_key.append(s)
            current_dict[s] = 1
    current_key.sort()
    failures = []
    n = len(stages)
    for k in current_key:
        failures.append([k, current_dict[k] / n])
        n -= current_dict[k]
    failures.sort(key=lambda x: x[1], reverse=True)

    answer = []
    visited = [0] * N
    for f in failures:
        answer.append(f[0])
        visited[f[0] - 1] = 1
    for ix, v in enumerate(visited):
        if v == 0:
            answer.append(ix + 1)
    return answer