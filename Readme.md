# Algorithm

알고리즘 문제 풀이한 코드를 정리하고, 자료구조/알고리즘 관련 지식을 정리한 공간입니다🧐

## 1. 문제 풀이 사이트

### 1. 백준(BJ)

[백준 바로가기](https://www.acmicpc.net)

### 2. SW Expert Academy(SWEA)

[SWEA 바로가기](https://www.swexpertacademy.com)

### 3. 프로그래머스

[프로그래머스 바로가기](https://programmers.co.kr/)

<br />

## 2. 알고리즘 풀이 Python TIP

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

### 순열, 조합

`itertools`를 사용해 단순한 순열, 조합을 구할 때 사용.

```python
from itertools import permutations, combinations

nums = [1, 2, 3, 4, 5]

print(list(permutations(nums, 2)))
# [(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3) ...

print(list(combinations(nums, 2)))
# [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4) ...
```

2개 이상의 리스트에서 `데카르트 곱(product, 가능한 모든 조합)`을 구할 수도 있다.

```python
from itertools import product

nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list(product(*nums)))
# [(1, 4, 7), (1, 4, 8), (1, 4, 9), (1, 5, 7), (1, 5, 8) ...
```

중복 조합 구하기(combinations_with_replacement)
combinations_with_replacement(반복 가능 객체, 중복 개수)

```python
from itertools import combinations_with_replacement

for el in combinations_with_replacement([1, 2, 3, 4], 2):
    print(el)
    # (1, 1) (1, 2) (1, 3) (1, 4) (2, 2) (2, 3) (2, 4) (3, 3) (3, 4) (4, 4)
```

### 문자열 알파벳, 문자 여부

`isalpha()`를 사용해 알파벳 여부를 검증. 또는 `isalnum()`를 사용해 알파벳, 숫자 여부를 검증.

```python
string = 'abcdefg'
print(string.isalpha()) # True
print(string.isalnum())  # True

```

### 알파벳을 숫자로 바꾸기

`ord()`를 사용하면 문자의 유니코드 값을 돌려준다. ord('A')의 경우 65, ord('a')의 경우 97로 치환된다.

```python
print(ord('A'))  # 65
print(ord('a'))  # 97
```

### dict에서 keyerror 없이 사용하기, defaultdict

`defaultdict`를 사용하면 key가 있는지 없는지 확인할 필요없이 key에 따른 값을 할당하거나 추가(append)할 수 있다

```python
import collections

dd = collections.defaultdict(list) # list: value의 초기 형태, []

dd['fruit'].append('apple') # keyerror가 발생하지 않는다
```

### Counter

dict 변수에 저장된 값 중 가장 높은 value를 갖는 객체를 찾을 때 `collection`의 `Counter`를 사용할 수 있다.

```python
from collections import Counter

words = {'apple': 5, 'pear': 3, 'banana': 10}
counts = Counter(words)

# 첫 번째로 value 값을 갖는 요소 출력
print(counts.most_common(1))

# [('banana', 10)]
```

### Min Heap

최소 힙을 사용하기 위해 `heapq`을 사용할 수 있다

```python
import heapq

heap = []
heapq.heappush(heap, 3)     # 힙 삽입
heapq.heappush(heap, 5)
heapq.heappush(heap, 4)

# 최솟값 가져오기
while heap:
    print(heapq.heappop())     # 3 4 5
```

### Binary to Int, Int to Binary

```python
int_value = int("1010", 2)  # binary to int
print(int_value)            # 10

binary_value = format(10, "b")  # int to binary
print(binary_value)             # "1010"
```

### bin, oct, hex
각각 2진수(binary), 8진수(octal), 16진수(hexadecimal) 변환
```python
bin(42) # '0b101010'
oct(42) # '0o52'
hex(42) # '0x2a'
```

integer로 변환
```python
int('0b101010',2)   # 42
int('0o52', 8)      # 42
int('0x2a', 16)     # 42
```

format 내장 함수를 활용하면 진수 문자열 앞에 포함된 접두어를 제외할 수 있다
```python
format(42, 'b')     # '101010'
format(42, 'o')     # '52'
format(42, 'x')     # '2a'

# 접두어를 포함시킬 수도 있다
format(42, '#b')    # '0b101010'
```
출처: [[파이썬] 2진수, 8진수, 16진수 다루기](https://www.daleseo.com/python-int-bases/) 

### 2진법 ~ 16번 진법 모두 구하기
```python
import string

tmp = string.digits + string.ascii_uppercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]
```
출처: [[Python] 진법 변환 총 정리?!](https://security-nanglam.tistory.com/508)

### Python 부동 소수점 정확히 표현하기
decimal 패키지 사용
```python
import decimal

d = decimal.Decimal('0.00001')
d += decimal.Decimal('0.00001')

print(decimal.Decimal('0.00001') === decimal.Decimal('0.00001'))    # True
```