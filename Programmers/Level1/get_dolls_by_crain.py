def solution(board, moves):
    answer = 0
    dolls = []

    for move in moves:
        for b in board:
            if b[move - 1] != 0:
                if len(dolls) > 0 and dolls[-1] == b[move - 1]:
                    dolls.pop()
                    answer += 2
                else:
                    dolls.append(b[move - 1])
                b[move - 1] = 0
                break

    return answer
