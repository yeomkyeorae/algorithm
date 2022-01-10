# Max heap 가정
# array로 힙 구성

heap = [7, 6, 5, 8, 3, 5, 9, 1, 6]
number = len(heap)


# 전체 트리 구조를 최대 힙 구조로 바꾼다
for i in range(1, number):
    c = i
    while c != 0:
        root = (c - 1) // 2
        if heap[root] < heap[c]: 
            heap[root], heap[c] = heap[c], heap[root]
        c = root    
    

# 크기를 줄여가면서 반복적으로 힙을 구성
for i in range(number - 1, -1, -1):
    # 큰 값(root)을 뒤로 계속 보낸다
    heap[0], heap[i] = heap[i], heap[0]
    
    root = 0
    c = 1
    
    while c < i:
        c = 2 * root + 1
        
        # 자식 중에서 더 큰 값 찾기
        if c < i - 1 and heap[c] < heap[c + 1]: # 오른쪽 자식이 더 크다면
            c += 1  # 오른쪽 자식 위치로 변경
        
        # 루트보다 자식이 더 크다면
        if c < i and heap[root] < heap[c]:
            heap[root], heap[c] = heap[c], heap[root]
            
        root = c
          
            
print(heap)