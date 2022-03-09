N = int(input())

s_set = []
for _ in range(N):
    s = set()
    s_set.append(s)

students = []
for _ in range(N):
    student = list(map(int, input().split(' ')))
    students.append(student)
    
for i, student in enumerate(students[:len(students)]):
    for j, opponent in enumerate(students[i + 1:]):
        for s, o in zip(student, opponent):
            if s == o:
                s_set[i].add(j + i + 1)
                s_set[j + i + 1].add(i)
                break

max_value = -1       
answer = -1 
for i, s in enumerate(s_set):
    cnt = len(s)
    if cnt > max_value:
       max_value = cnt
       answer = i + 1
    
print(answer) 