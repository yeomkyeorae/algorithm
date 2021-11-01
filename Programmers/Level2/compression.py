def solution(msg):
    words = {}
    for i in range(26):
        words[chr(i + 65)] = i + 1
        
    length = len(msg)
    start = 0
    new_index = 27
    answer = []
    last = ''
    while start < length:
        string = ''
        for i in range(length - start):
            string += msg[start]
            value = words.get(string)
            if not value:
                break
            start += 1
        if len(string) and start < length:
            words[string] = new_index
            value = words.get(string[:len(string) - 1])
            if value:
                answer.append(value)
        else:
            last = string
        new_index += 1

    answer.append(words[last])
    
    return answer