input_list = list(map(int, input().split()))

result_list = []
for i in range(len(input_list)-1):
    result = 0
    for j in range(i+1, len(input_list)):
        if input_list[i] > input_list[j]:
            result += 1
    result_list.append(result)

max_value = -1
for value in result_list:
    if value > max_value:
        max_value = value

print(max_value)