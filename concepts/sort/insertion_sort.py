arr = [3, 2, 5, 1, 6, 4]

for i in range(len(arr) - 1):
    for j in range(i + 1, 0, -1):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
        else:
            break
        
print(arr)