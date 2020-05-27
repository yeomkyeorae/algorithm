tries = int(input())

for t in range(1, tries + 1):
    angle = int(input())
    total_minutes = angle * 2
    hour = total_minutes // 60
    minute = total_minutes % 60
    print('#{} {} {}'.format(t, hour, minute))
