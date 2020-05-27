value = int(input())

answer = []
for num in range(1, value + 1):
    cnt = 0
    num_to_str = str(num)
    for ch in str(num_to_str):
        if '3' == ch:
            cnt += 1
        elif '6' == ch:
            cnt += 1
        elif '9' == ch:
            cnt += 1
    if cnt == 0:
        answer.append(num_to_str)
    else:
        tmp = ''
        for _ in range(cnt):
            tmp += '-'
        answer.append(tmp)

print(' '.join(answer))
