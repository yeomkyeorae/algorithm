from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = []
    passed = []
    truck_weights = deque(truck_weights)
    num_trucks = len(truck_weights)

    answer = 0
    while num_trucks > len(passed):
        answer += 1

        flag = False
        for ix, b in enumerate(bridge):
            b[1] -= 1
            if b[1] == 0:
                flag = True
        if flag:
            pop = bridge.pop(0)[0]
            passed.append(pop)
            weight += pop

        if truck_weights and weight >= truck_weights[0]:
            pop = truck_weights.popleft()
            bridge.append([pop, bridge_length])
            weight -= pop

    return answer