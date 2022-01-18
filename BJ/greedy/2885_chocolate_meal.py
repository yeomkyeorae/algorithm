K = int(input())

size = 1
while True:
    if size >= K:
        break
    
    size *= 2
    
if size == K:
    print(size, 0)
else:
    chocolates = [size]
    split_cnt = 0
    summation = 0
    while True:
        split_cnt += 1
        
        small = chocolates.pop()
        small //= 2
        
        chocolates.append(small)
        chocolates.append(small)
        
        if summation + small == K:
            print(size, split_cnt)
            break
        elif summation + small < K:
            summation += small