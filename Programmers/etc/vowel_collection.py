import decimal


def cut_zero(value_str):
    tmp = ''
    flag = True
    for i in range(len(value_str) - 1, -1, -1):
        if flag:
            if value_str[i] == '0':
                continue
            flag = False    
        tmp += value_str[i]
    
    return tmp[::-1]


def solution(word):
    value_dict = {
        '1': "A",
        '2': "E",
        '3': "I",
        '4': "O",
        '5': "U"
    }
    
    answer = 1
    
    current = decimal.Decimal('0.1')
    word_candi = ""
    while True:
        value_str = str(current).split('.')[1:][0]
        value_str = cut_zero(value_str)
    
        flag = True
        for v in value_str:
            try:
                word_candi += value_dict[v]
            except KeyError:
                flag = False
                word_candi = ""
                break
        
        if flag:
            if word_candi == word:
                break
            else:
                word_candi = ""
                answer += 1
        current += decimal.Decimal('0.00001')
    
    return answer