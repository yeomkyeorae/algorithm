# <SWEA 알고리즘> 

# 실패한 문제



# 성공한 문제

## D2

#### [중간 평균값 구하기]([https://www.swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5Pw_-KAdcDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14](https://www.swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5Pw_-KAdcDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=[D1~D2+문제풀이]+기초+다지기+Part2&problemBoxCnt=14))

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_mid_mean_value.py)

![이미지 이름](./images/D2_mid_mean_value.PNG)

> 성공 전략

- 문제를 정확히 파악하였음.
- round 함수를 통해 반올림을 실시.



#### [조교의 성적 매기기]([https://www.swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PwGK6AcIDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14](https://www.swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PwGK6AcIDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=[D1~D2+문제풀이]+기초+다지기+Part2&problemBoxCnt=14))

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_assist_grading.py)

![이미지 이름](./images/D2_assist_grading.PNG)

> 성공 전략

- 먼저 K 번째 학생의 등수를 파악하고자 함.
- 그리고 그 등수를 바탕으로 그 학생의 학점이 무엇인지 알아내고자 함. 
- 학생의 수가 10의 배수이기 때문에 각 학점이 부여되는 횟수가 동일하다는 점에 착안해 학생 수에 따른 학점 부요 횟수의 규칙성을 파악함.



#### [스도쿠 검증]([https://www.swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5Psz16AYEDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14](https://www.swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5Psz16AYEDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=[D1~D2+문제풀이]+기초+다지기+Part2&problemBoxCnt=14))

[코드로 이동하기]()

![이미지 이름](./images/D2_sdoku_checking.PNG)

> 성공 전략

- row 방향, col 방향, square 형태의 총 3가지를 검증하고자 함.
- 따라서, 수도쿠를 입력 받자마자 위 3가지 형태를 저장하는 각각의 리스트를 생성함.
- 위에서 생성한 리스트를 바탕으로 검증.

> 발전

- 리스트로 저장하지 않고 메모리를 절약하면서 바로 검증할 수도 있을 거 같다.
- 수도쿠의 규칙성에 의거하여 위 3가지 형태를 고려하지 않고도 검증할 수 있지 않을까?



#### [시각 덧셈]([https://www.swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PttaaAZIDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14](https://www.swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PttaaAZIDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=[D1~D2+문제풀이]+기초+다지기+Part2&problemBoxCnt=14))

[코드로 이동하기]()

![이미지 이름](./images/D2_add_time.PNG)

> 성공 전략

- 분을 더했을 때 60이 넘으면 시간을 더하고
- 시간을 더했을 때 12가 넘으면 1~12 사이 단위로 변환

