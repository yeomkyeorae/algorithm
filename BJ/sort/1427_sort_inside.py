value = int(input())
value_list = []
while value > 0:
    value_list.append(value % 10)
    value //= 10
sorted_list = sorted(value_list, reverse=True)
for value in sorted_list:
    print(value, end='')
