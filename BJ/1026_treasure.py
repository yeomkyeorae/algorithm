# 입력
num = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 최소인 수와 최대인 수끼리 곱하는 것이 최적일 것이라 생각.
# 따라서 입력 받은 리스트를 하나는 오름차순으로, 나머지는 내림차순으로 정렬
a = sorted(a)
b = sorted(b, reverse=True)

# 결과값 s를 초기화하고 a, b 리스트에 있는 값들을 순차적으로 곱하고 결과값에 더함.
s = 0
for i in range(num):
    s += a[i] * b[i]
print(s)
