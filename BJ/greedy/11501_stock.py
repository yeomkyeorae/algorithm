import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))

    max_price = days[-1]
    answer = 0
    
    i = len(days) - 2
    while i >= 0:
        price = days[i]
        if price < max_price:
            answer += max_price - price
        elif price > max_price:
            max_price = price
        i -= 1
                    
    print(answer)