s = input()
p = input()

answer = 0

total_string = ''
sub_string = ''
for i in range(len(p)):
    if sub_string + p[i] in s:
        sub_string += p[i]
    else:
        total_string += sub_string
        sub_string = p[i]
        answer += 1

answer += 1

print(answer)
