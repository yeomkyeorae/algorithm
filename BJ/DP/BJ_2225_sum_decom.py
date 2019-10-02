# d[k][n] = Summation(d[k - 1][n - l]), 0 <= l <= n

n, k = map(int, input().split())

d = []
for _ in range(k):
    d.append([0] * n)

# for kk in range(1, k):
#     for i in range(n):
#         tmp = 0
#         for l in range(n):
#             tmp += d[kk - 1][n - l - 1]
#         d[kk][i] = tmp

print(d)