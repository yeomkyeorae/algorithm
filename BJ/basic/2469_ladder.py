perm = []

def make_permutation(stage, K, arr):
    if stage == K - 1:
        perm.append(''.join(arr) + '*')
        return
    
    if stage == 0 or arr[-1] != '-':
        arr.append('-')
        make_permutation(stage + 1, K, arr)
        arr.pop()
    
    arr.append('*')
    make_permutation(stage + 1, K, arr)
    arr.pop()
    
    
K = int(input())
make_permutation(0, K, [])

N = int(input())

target = input()
before = []
after = []
before_flag = True
for _ in range(N):
    row = input()
    
    if '?' in row:
        before_flag = False
        continue
     
    if before_flag:
        before.append(row + '*')
    else:
        after.append(row + '*')

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
             'H', 'I', 'J', 'K', 'L', 'M', 'N', 
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
             'V', 'W', 'X', 'Y', 'Z']

# before 계산
arr = []
for i, alpha in enumerate(alphabets[:K]):
    row = 0
    col = i

    not_done = True
    from_to_left = False
    from_to_right = False
    while not_done and before:
        if len(before) - 1 == row:
            not_done = False
            
        if col > 0 and before[row][col - 1] == '-' and not from_to_left:
            from_to_right = True
            col -= 1
        elif before[row][col] == '*':
            from_to_left = False
            from_to_right = False
            row += 1
        elif before[row][col] == '-' and not from_to_right:
            from_to_left = True
            col += 1
        else:
            from_to_left = False
            from_to_right = False
            row += 1
        
    arr.append([alpha, col])
    
arr.sort(key=lambda x:x[1])

# after 계산
ix_dict = {}
for i in (range(K)):
    row = 0
    col = i

    not_done = True
    from_to_left = False
    from_to_right = False
    while not_done and after:
        if len(after) - 1 == row:
            not_done = False
            
        if col > 0 and after[row][col - 1] == '-' and not from_to_left:
            from_to_right = True
            col -= 1
        elif after[row][col] == '*':
            from_to_left = False
            from_to_right = False
            row += 1
        elif after[row][col] == '-' and not from_to_right:
            from_to_left = True
            col += 1
        else:
            from_to_left = False
            from_to_right = False
            row += 1
    
    ix_dict[i] = col

find_answer = False
for p in perm:
    board = p
    tmp = []
    
    for alpha, loc in arr:
        col = loc
        if loc > 0 and board[loc - 1] == '-':
            col -= 1
        if board[loc] == '-':
            col += 1

        tmp.append([alpha, col])

    tmp = list(map(lambda x:[x[0], ix_dict[x[1]]], tmp))
    tmp.sort(key=lambda x: x[1])
    tmp = ''.join(list(map(lambda x:x[0], tmp)))
    
    if tmp == target:
        print(p[:len(p) - 1])
        find_answer = True
        break
    
if not find_answer:
    print('x' * (K - 1))
