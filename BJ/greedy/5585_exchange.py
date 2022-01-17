N = int(input())

exchange = 1000 - N

answer = 0
for coin in [500, 100, 50, 10, 5, 1]:
    num = exchange // coin
    answer += num

    exchange -= num * coin

print(answer)