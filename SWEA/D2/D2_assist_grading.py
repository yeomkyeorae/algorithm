import math

test_case = int(input())
for i in range(1, test_case+1):
    n, k = map(int, input().split())

    # 학점당 부여 개수
    num_each_grade = n / 10
    grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    score_list = []
    for j in range(1, n+1):
        mid, final, subject = map(int, input().split())
        total_score = mid * 0.35 + final * 0.45 + subject * 0.2
        score_list.append(total_score)
    # 스코어 내림차순
    new_score_list = sorted(score_list, reverse=True)
    # 등수 index
    # score_list에 있는 특정 점수가 내림차순으로 변경된 new_score_list에서 어느 index에 있는지 파악
    grade_index = new_score_list.index(score_list[k-1])

    print('#{} {}'.format(i, grade_list[math.ceil((grade_index + 1) / num_each_grade) - 1]))

