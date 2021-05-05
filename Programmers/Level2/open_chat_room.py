def solution(record):
    answer = []
    id_name_dict = {}
    for r in record:
        splited = r.split(" ")

        user_id = splited[1]
        if len(splited) == 2:
            answer.append(user_id + ' 님이 나갔습니다.')
        else:
            command = splited[0]
            nickname = splited[2]

            if command == 'Enter':
                id_name_dict[user_id] = nickname
                answer.append(user_id + ' 님이 들어왔습니다.')

            elif command == 'Change':
                id_name_dict[user_id] = nickname

    for i, a in enumerate(answer):
        splited = a.split(" ")
        user_id = splited[0]
        answer[i] = id_name_dict[user_id] + splited[1] + ' ' + splited[2]

    return answer
