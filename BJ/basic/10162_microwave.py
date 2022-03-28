n = int(input())

if n % 10 != 0:
    print(-1)
else:
    a_cnt = n // 300
    n -= a_cnt * 300
    
    b_cnt = n // 60
    n -= b_cnt * 60
    
    c_cnt = n // 10
    print('{} {} {}'.format(a_cnt, b_cnt, c_cnt))