d_dict = { 'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
clock = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
i_clock = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}


C, R = map(int, input().split())
N, M = map(int, input().split())

robot_dict = {}
for i in range(N):
    c, r, d = input().split()
    r, c = R - int(r), int(c) - 1
    robot_dict[i + 1] = [r, c, d]

flag = True
for i in range(M):
    robot_num, command, for_num = input().split()
    robot_num, for_num = int(robot_num), int(for_num)

    if flag:
        for _ in range(for_num):
            if command == 'L':
                robot_dict[robot_num][2] = i_clock[robot_dict[robot_num][2]]
            elif command == 'R':
                robot_dict[robot_num][2] = clock[robot_dict[robot_num][2]]
            elif command == 'F':
                if not 0 <= robot_dict[robot_num][0] + d_dict[robot_dict[robot_num][2]][0] < R:
                    ANSWER = 'Robot {} crashes into the wall'.format(robot_num)
                    flag = False
                    break
                elif not 0 <= robot_dict[robot_num][1] + d_dict[robot_dict[robot_num][2]][1] < C:
                    ANSWER = 'Robot {} crashes into the wall'.format(robot_num)
                    flag = False
                    break
                else:
                    robot_dict[robot_num][0] = robot_dict[robot_num][0] + d_dict[robot_dict[robot_num][2]][0]
                    robot_dict[robot_num][1] = robot_dict[robot_num][1] + d_dict[robot_dict[robot_num][2]][1]
                    for k in robot_dict.keys():
                        if k == robot_num:
                            continue
                        if robot_dict[robot_num][0] == robot_dict[k][0] and robot_dict[robot_num][1] == robot_dict[k][1]:
                            ANSWER = 'Robot {} crashes into robot {}'.format(robot_num, k)
                            flag = False
                            break
                if not flag:
                    break
if flag:
    print('OK')
else:
    print(ANSWER)
