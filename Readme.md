# Algorithm

알고리즘 문제 풀이한 코드를 정리하고, 자료구조/알고리즘 관련 지식을 정리한 공간입니다🧐

## 문제 풀이 사이트

### 1. 백준(BJ)

[백준 바로가기](https://www.acmicpc.net)

### 2. SW Expert Academy(SWEA)

[SWEA 바로가기](https://www.swexpertacademy.com)

### 3. 프로그래머스

[프로그래머스 바로가기](https://programmers.co.kr/)

## 알고리즘 풀이 python TIP

### 이진 탐색: bisect

python에서 제공하는 bisect 모듈을 사용하면 이진 탐색을 구현하지 않고도 쉽게 이용할 수 있다.
정렬된 배열이 있을 때, 주어진 값을 배열의 order를 해치지 않으면서 어디(index)에 위치 시킬 수 있을지 찾아보자

- bisect_left(iterable, value): 위치할 왼쪽 인덱스를 구한다
- bisect_right(iterable, value): 위치할 오른쪽 인덱스를 구한다

```python
import bisect

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(bisect.bisect_left(arr, 5)) # 4: 새롭게 5가 들어온다면 이진 탐색으로 찾은 값을 기준으로 왼쪽에 위치
print(bisect.bisect_right(arr, 5)) # 5: 새롭게 5가 들어온다면 이진 탐색으로 찾은 값을 기준으로 오른쪽에 위치
```
