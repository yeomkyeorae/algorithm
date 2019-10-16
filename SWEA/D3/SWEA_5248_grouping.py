def find_set(x):
    if x != p[x]:       # 루트 노트가 아니면
        p[x] = find_set(p[x])   # 부모의 부모로...
    return p[x]         # 루트 노트 찾으면 return


tries = int(input())

for t in range(1, tries + 1):
    n, m = map(int, input().split())

    p = [x for x in range(n + 1)]   # 개별 노드를 하나의 집합으로 표현

    ans = n
    m_list = list(map(int, input().split()))
    for i in range(0, len(m_list), 2):
        u, v = m_list[i], m_list[i + 1]
        a = find_set(u)     # 부모 찾기
        b = find_set(v)     # 부모 찾기
        if a != b:          # 부모가 다르면, 한쪽 부모로 만들어 주기
            p[b] = a
            ans -= 1        # 그룹 수 하나 감소

    print('#{} {}'.format(t, ans))
