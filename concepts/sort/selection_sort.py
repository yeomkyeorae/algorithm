import sys
MAX_VALUE = sys.maxsize

arr = [3, 2, 5, 1, 6, 4]

for i in range(len(arr) - 1):
    min_value = MAX_VALUE
    min_index = -1
    
    for j in range(i, len(arr)):
        if min_value > arr[j]:
            min_value = arr[j]
            min_index = j
    
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)