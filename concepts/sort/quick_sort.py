def quick_sort(data, start, end):
    if start >= end:    # 원소가 1개인 경우
        return

    p = start           # 피봇: 첫 번째 원소로
    left = start + 1    # 왼쪽 출발 지점 -> 
    right = end         # 오른쪽 출발 지점 <-
    
    while left <= right:       # 엇갈릴 때까지 반복
        while left <= end and data[left] <= data[p]:        # 키 값 보다 큰 값을 만날 때 까지
            left += 1
        while right > start and data[right] >= data[p]:     # 키 값 보다 작은 값을 만날 때 까지
            right -= 1

        if left > right:       # 현재 엇갈린 상태면 키 값과 교체
            data[right], data[p] = data[p], data[right]
        else:
            data[right], data[left] = data[left], data[right]
          
    quick_sort(data, start, right - 1)
    quick_sort(data, right + 1, end)


data = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

quick_sort(data, 0, len(data) - 1)
print(data)