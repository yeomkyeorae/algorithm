N = int(input())

num_sequences = []
for _ in range(N):
    num_sequences.append(int(input()))    

answer = []
stack = []
seq_index = 0
for i in range(1, N + 1):    
    stack.append(i)
    answer.append('+')
    
    while seq_index < N and stack:
        if stack[-1] == num_sequences[seq_index]:
            stack.pop()
            seq_index += 1
            answer.append('-')
        else:
            break

if seq_index == N:
    for el in answer:
        print(el)
else:
    print('NO')