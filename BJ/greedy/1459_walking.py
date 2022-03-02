x, y, wid, diag = list(map(int, input().split(' ')))

if x < y:
    x, y = y, x

dist = 0
if wid * 2 > diag:
    for _ in range(y):
        dist += diag

    remain = x - y
    q, r =  divmod(remain, 2)
    
    remain_dist = diag
    if diag > wid:
        remain_dist = wid
    
    dist += (remain_dist * q * 2) + r * wid

else:
    dist = (x + y) * wid

print(dist)