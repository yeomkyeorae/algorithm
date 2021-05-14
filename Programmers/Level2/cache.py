def solution(cacheSize, cities):
    answer = 0
    cache = {}
    for city in cities:
        city = city.lower()

        # 캐시 히트
        if city in cache.keys():
            answer += 1
            for key in cache.keys():
                if key == city:
                    cache[key] = 0
                else:
                    cache[key] += 1
        # 캐시 미스
        else:
            if len(cache.keys()) == cacheSize and cacheSize != 0:
                max_k, max_v = 0, 0
                for k, v in cache.items():
                    if max_v <= v:
                        max_v = v
                        max_k = k
                del cache[max_k]

            for key in cache.keys():
                cache[key] += 1

            if cacheSize != 0:
                cache[city] = 0
            answer += 5

    return answer
