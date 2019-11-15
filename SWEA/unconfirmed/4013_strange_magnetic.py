from collections import deque


def rotate(mag_num, direction):
    original_direction = direction
    rotate_list = [[mag_num, direction]]
    for ix in range(mag_num, 4):
        if d[ix][2] != d[ix + 1][6]:
                direction *= -1
                rotate_list.append([ix + 1, direction])
        else:
            break
    direction = original_direction
    for ix in range(mag_num, 1, -1):
        if d[ix][6] != d[ix - 1][2]:
            direction *= -1
            rotate_list.append([ix - 1, direction])
        else:
            break

    for rot in rotate_list:
        if rot[1] == -1:
            d[rot[0]].append(d[rot[0]].popleft())
        elif rot[1] == 1:
            d[rot[0]].appendleft(d[rot[0]].pop())


tries = int(input())

for t in range(1, tries + 1):
    n = int(input())

    d = [0]
    for i in range(4):
        d.append(deque(map(int, input().split())))

    for _ in range(n):
        mag_num, direction = map(int, input().split())
        rotate(mag_num, direction)

    score = 1 * d[1][0] + 2 * d[2][0] + 4 * d[3][0] + 8 * d[4][0]
    print('#{} {}'.format(t, score))
