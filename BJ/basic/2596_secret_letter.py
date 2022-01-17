dictionary = [['000000', 'A'], ['001111', 'B'], ['010011', 'C'], ['011100', 'D'],
 ['100110', 'E'], ['101001', 'F'], ['110101', 'G'], ['111010', 'H']]

N = int(input())

string = input()

i = 0
answer = ''
for j in range(len(string) // 6):
    sub = string[i:i+6]
    found = False
    
    candi = []
    for d in dictionary:
        target = d[0]
        
        same_cnt = 0
        for s, t in zip(sub, target):
            if s == t:
                same_cnt += 1

        if same_cnt == 6:
            answer += d[1]
            found = True
            candi = []
            break
        
        if same_cnt == 5:
            candi.append(d[1])
        
    if len(candi) == 1:
        answer += candi[0]
        found = True
        
    if not found:
        answer = j + 1
        break
        
    i += 6
    
print(answer)
