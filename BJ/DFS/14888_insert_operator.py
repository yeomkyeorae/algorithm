def solve(plus, minus, mul, div, result, idx):

    global MAX_VALUE
    global MIN_VALUE

    if idx == n:
        MAX_VALUE = max(MAX_VALUE, result)
        MIN_VALUE = min(MIN_VALUE, result)
        return

    if plus > 0:
        solve(plus - 1, minus, mul, div, result + num_list[idx], idx + 1)
    if minus > 0:
        solve(plus, minus - 1, mul, div, result - num_list[idx], idx + 1)
    if mul > 0:
        solve(plus, minus, mul - 1, div, result * num_list[idx], idx + 1)
    if div > 0:
        if result < 0 < num_list[idx]:
            result = result * -1
            solve(plus, minus, mul, div - 1, (result // num_list[idx]) * -1, idx + 1)
        else:
            solve(plus, minus, mul, div - 1, result // num_list[idx], idx + 1)


n = int(input())

num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

MAX_VALUE = -1000000000
MIN_VALUE = 1000000000

solve(op_list[0], op_list[1], op_list[2], op_list[3], num_list[0], 1)

print(MAX_VALUE)
print(MIN_VALUE)
