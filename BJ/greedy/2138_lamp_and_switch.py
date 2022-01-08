N = int(input())

string = input()
target = input()


def turn_on(string, target, change_first):
    cnt = 0
    if change_first:
        cnt += 1
        tmp = ''
        sub_string = string[:2]
        for ch in sub_string:
            if ch == '0':
                tmp += '1'
            else:
                tmp += '0'
        tmp += string[2:]
        string = tmp
        
    for i in range(1, N):
        if string[i - 1] != target[i - 1]:
            cnt += 1
            
            start_index = i - 1
            end_index = i + 2
            
            if i == N - 1:
                end_index -= 1
            
            tmp = string[:start_index]
            sub_string = string[start_index:end_index]
            for ch in sub_string:
                if ch == '0':
                    tmp += '1'
                else:
                    tmp += '0'
            
            tmp += string[end_index:]
            string = tmp

    if string == target:
        return cnt
    else:
        return -1
    


answer1 = turn_on(string[:], target, True)
answer2 = turn_on(string[:], target, False)

answer = 0
if answer1 == -1:
    answer = answer2
elif answer2 == -1:
    answer = answer1
else:
    answer = min(answer1, answer2)
print(answer)