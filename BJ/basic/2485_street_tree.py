def GCD(x, y):
    while y:
        x, y= y, x % y
    return x


N = int(input())

init = True
before = 0
diff_list = []
for _ in range(N):
    tree = int(input())
    if init:
        before = tree
        init = False
        continue
    
    diff = tree - before
    diff_list.append(diff)
    before = tree

diff_set = set(diff_list)
init = True
for i in range(len(diff_set)):
    if init:
        a = diff_list[i]
        init = False
        continue
    
    b = diff_list[i]
    a = GCD(a, b)
    
gcd = a
answer = 0
for d in diff_list:
    answer += (d // gcd) - 1

print(answer)