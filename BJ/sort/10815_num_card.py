def binary_search(input_list, key):

    low = 0
    high = len(input_list) - 1

    while high >= low:
        mid = int((low + high) / 2)

        if input_list[mid] > key:
            high = mid - 1
        elif input_list[mid] < key:
            low = mid + 1
        else:
            return '1'

    return '0'


n = int(input())
card_list = list(map(int, input().split()))

m = int(input())
check_list = list(map(int, input().split()))

card_list = sorted(card_list)

result = []
for value in check_list:
    result.append(binary_search(card_list, value))

print(' '.join(result))
