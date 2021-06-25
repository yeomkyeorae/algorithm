numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def solution(files):

    head_dict = {}
    for ix, file in enumerate(files):
        head = ''
        for jx, ch in enumerate(file):
            if ch in numbers:
                break
            head += ch
        head = head.lower()

        num = ''
        for ch in file[jx:]:
            if ch in numbers:
                num += ch
            else:
                break

        num = int(num)

        if head in head_dict.keys():
            if num in head_dict[head].keys():
                head_dict[head][num].append(ix)
            else:
                head_dict[head][num] = [ix]
        else:
            head_dict[head] = {num: [ix]}

    answer = []

    head_order = list(head_dict.keys())
    head_order.sort()
    for h in head_order:
        num_order = list(head_dict[h].keys())
        num_order.sort()

        for n in num_order:
            indexes = head_dict[h][n]
            indexes.sort()

            for ix in indexes:
                answer.append(files[ix])

    return answer
