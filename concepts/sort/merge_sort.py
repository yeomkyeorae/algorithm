a = [7, 6, 5, 8, 3, 5, 9, 1]
sorted = [0] * len(a)


def merge(a, m, middle, n): # m: 시작점, middle: 중간점, n: 끝점
    i = m
    j = middle + 1
    k = m
    # 작은 순서대로 삽입
    while i <= middle and j <= n:
        if a[i] <= a[j]:
            sorted[k] = a[i]
            i += 1
        else:
            sorted[k] = a[j]
            j += 1
        k += 1
    
    # 남은 데이터 삽입
    if i > middle:
        for t in range(j, n + 1):
            sorted[k] = a[t]
            k += 1
    else:
        for t in range(i, middle + 1):            
            sorted[k] = a[t]
            k += 1

    # 정렬된 배열 삽입
    for t in range(m, n + 1):
        a[t] = sorted[t]
        
def mergeSort(a, m, n):
    if m < n:
        middle = (m + n) // 2
        
        mergeSort(a, m, middle)
        mergeSort(a, middle + 1, n)
        
        merge(a, m, middle, n)
        

mergeSort(a, 0, len(a) - 1)

print(a)