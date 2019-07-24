# <SWEA 알고리즘> - D2

# 실패한 문제 & 진행중인 문제



# 성공한 문제

#### 중간 평균값 구하기

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_mid_mean_value.py)

![이미지 이름](./images/D2_mid_mean_value.PNG)

> 성공 전략

- 문제를 정확히 파악하였음.
- round 함수를 통해 반올림을 실시.



#### 조교의 성적 매기기

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_assist_grading.py)

![이미지 이름](./images/D2_assist_grading.PNG)

> 성공 전략

- 먼저 K 번째 학생의 등수를 파악하고자 함.
- 그리고 그 등수를 바탕으로 그 학생의 학점이 무엇인지 알아내고자 함. 
- 학생의 수가 10의 배수이기 때문에 각 학점이 부여되는 횟수가 동일하다는 점에 착안해 학생 수에 따른 학점 부요 횟수의 규칙성을 파악함.



#### 스도쿠검증

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_sdoku_checking.py)

![이미지 이름](./images/D2_sdoku_checking.PNG)

> 성공 전략

- row 방향, col 방향, square 형태의 총 3가지를 검증하고자 함.
- 따라서, 수도쿠를 입력 받자마자 위 3가지 형태를 저장하는 각각의 리스트를 생성함.
- 위에서 생성한 리스트를 바탕으로 검증.

> 발전

- 리스트로 저장하지 않고 메모리를 절약하면서 바로 검증할 수도 있을 거 같다.
- 수도쿠의 규칙성에 의거하여 위 3가지 형태를 고려하지 않고도 검증할 수 있지 않을까?



#### 시각 덧셈

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_add_time.py)

![이미지 이름](./images/D2_add_time.PNG)

> 성공 전략

- 분을 더했을 때 60이 넘으면 시간을 더하고
- 시간을 더했을 때 12가 넘으면 1~12 사이 단위로 변환



#### 지그재그숫자

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_zigzag.py)

![이미지 이름](./images/D2_zigzag.PNG)

> 성공전략

- `list comprehension`을 적절히 활용하였다. 짱짱



#### 초심자의 회문 검사

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_palindrome_checking.py)

![이미지 이름](./images/D2_palindrome_checking.PNG)

> 성공전략

- `str`객체를 거꾸로 만들기 위해서 string[ : : -1]과 같이 접근하였다.
- `list comprehension`!



#### 어디에 단어가 들어갈 수 있을까

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_can_word_be_in.py)

![이미지](./images/D2_can_word_be_in.PNG)

> 성공전략

- 전체 탐색하면서 0을 만나면 `is_possible`를 0으로 초기화하고, 1을 만나면 `is_possible`값을 +1한다.
- 0을 만나고 is_possible 값을 확인했을 때 특정 길이 K이면 개수에 +1한다. 



#### 쉬운 거스름돈

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_easy_changes.py)

![쉬운 거스름돈](./images/D2_easy_changes.PNG)

> 성공전략

- 큰 단위의 금액부터 잔돈을 지급하면서 나머지를 다음 단위 금액으로 지급하는 식으로 접근

>유의할 점

- 위의 전략이 통하지 않는 경우가 있음을 인지.

  

#### 숫자 배열 회전

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_num_array_rotation.py)

![숫자 배열 회전](./images/D2_num_array_rotation.PNG)

> 성공전략

- 90도 반시계 방향으로 회전했을 때 첫 번째 행이 마지막 열이 되고, 두 번째 행이 마지막에서 왼쪽 열이 됨을 인지.
- 180도는 90도 회전한 거 에서 다시 90도 회전을 해 구함. 270도도 마찬가지



#### 숫자를 정렬하자

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_sort_num.py)

![숫자를 정렬하자](./images/D2_sort_num.PNG)

> 성공전략

- 오름차순으로 정렬하기 위해 리스트에서 최솟값을 뽑아내고 다른 임시 리스트에 저장하는 방식으로 사용



#### 두 개의 숫자열

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2_two_num_lists.py)

![두 개의 숫자열](./images/D2_two_num_lists.PNG)

> 성공전략

- 작은 크기의 리스트를 기준으로, 그 리스트의 각 요소들을 큰 크기의 리스트 값과 곱해 새로운 리스트를 생성함. 예를 들면 위의 Ai에서 1값이 아래 Bj의 3, 6, -7과 곱한 값을 저장하는 식임. 
- 위와 같은 방식을 이용하면 [[1이 곱한 값], [5가 곱한 값], [3이 곱한 값]]을 저장할 수 있음.
- 일정 방향으로의 인덱스를 활용해 합을 구하고, 최대값을 출력함.





#### 달팽이 숫자

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/SWEA/D2/D2_snail_number.py)

![달팽이 숫자](./images/D2_snail_number.PNG)

> 성공전략

- (0, 0)에서 시작해 반시계 방향으로(오른쪽 -> 아래 -> 왼쪽 -> 위) 계속 이동하는 규칙성에 의거.
- 반시계 방향으로 이동하면서 그 반경은 지속적으로 감소하는 것에 착안.
- 위의 경우 오른쪽으로 3, 아래로 2(3-1), 왼쪽으로 2(3-1), 위로 1(2-1) 변화하는 것을 인지.
- 또한, 오른쪽이나 왼쪽으로 이동할 때는 row index가 고정되고, 위나 아래로 이동할 때는 col index가 고정되는 것을 반영.

> 개선방향

- 분명히 더 나은 방법이 있을텐데 ... 너무 노가다로 풀었다.