string = input()
target = input()

string_len = len(string)
target_len = len(target)
i = 0
answer = 0
while i < string_len:
    if i + target_len <= string_len:
        sub_string = string[i:i + target_len]
        if sub_string == target:
            answer += 1
            i = i + target_len
        else:
            i += 1
    else:
        break
    
print(answer)