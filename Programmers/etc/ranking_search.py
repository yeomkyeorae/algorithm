import bisect


def search(iters, score):
    left_index = bisect.bisect_left(iters, score)
    return len(iters) - left_index


def solution(info, query):
    new_info = {}
    for inf in info:
        i1, i2, i3, i4, i5 = inf.split(' ')
        score = int(i5)
        arr = [i1, i2, i3, i4]

        for v1 in [i1, '-']:
            for v2 in [i2, '-']:
                for v3 in [i3, '-']:
                    for v4 in [i4, '-']:
                        key = v1 + v2 + v3 + v4
                        if key in new_info:
                            new_info[key].append(score)
                        else:
                            new_info[key] = [score]

    for key in new_info.keys():
        new_info[key].sort()

    answer = []
    for q in query:
        q = q.replace(' and ', '')
        q, score = q.split(' ')
        score = int(score)
        cnt = 0

        if not q in new_info.keys():
            answer.append(cnt)
        else:
            answer.append(search(new_info[q], score))

    return answer
