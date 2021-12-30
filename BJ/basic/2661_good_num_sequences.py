N = int(input())
answer = ''
done = False


def check(string):
    for i in range(1, len(string) // 2 + 1):
        for j in range(0, len(string) - i):
            if string[j:j + i] == string[j + i: j + i * 2]:
                return False

    return True 


def go(string, level):
    global N
    global answer
    global done
    
    if done:
        return
    
    if not check(string):
        return

    if level == N:
        done = True
        answer = string      
        return
    
    for n in range(1, 4):
        go(string + str(n), level + 1)
    
    
go('', 0)

print(answer)