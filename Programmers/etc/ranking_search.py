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
                        if key in new_info.keys():
                            if score in new_info[key].keys():
                                new_info[key][score] += 1
                            else:
                                new_info[key][score] = 1
                        else:
                            new_info[key] = {score: 1}

    answer = []
    for q in query:
        q = q.replace(' and ', '')
        q, score = q.split(' ')
        score = int(score)

        cnt = 0
        try:
            keys = sorted(new_info[q].keys(), reverse=True)
            for key in keys:
                if key < score:
                    break
                cnt += new_info[q][key]
        except Exception:
            pass
        answer.append(cnt)

    return answer
