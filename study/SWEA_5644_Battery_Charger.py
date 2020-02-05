d = {
    0: [0, 0],
    1: [-1, 0],
    2: [0, 1],
    3: [1, 0],
    4: [0, -1]
}

tries = int(input())

for t in range(1, tries + 1):
    M, A = map(int, input().split())    # M: 이동 시간, A: 배터리 개수
    person1 = list(map(int, input()))
    person2 = list(map(int, input()))

    board = []
    for _ in range(10):
        board.append([0] * 10)

    battery = []    # [[col + 1, row + 1, range, power], ... ]
    for _ in range(A):
        battery.append(list(map(int, input().split())))

