arr = [55, 7, 78, 12, 42]

n = len(arr)
for i in range(1, n):
    for j in range(n - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)