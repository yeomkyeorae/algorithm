# 백준 알고리즘(DP, Dynamic Programming)

## 실패한 문제 || 풀다만 문제

#### [11726번 2xn 타일링](https://www.acmicpc.net/problem/11725)

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/BJ/DP/BJ_11726_2xn_tile.py)

![2xn 타일링](./images/11726.PNG)



## 성공한 문제

#### [1463번 1로 만들기](https://www.acmicpc.net/problem/1463)

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/BJ/DP/BJ_1463_making_as_one.py)

![1로 만들기](./images/1463.PNG)



> 전략

- bottom up방식으로 d 리스트를 채워나감.
- 먼저 1을 더하는 것(빼는 것)을 먼저 고려하고, 그 다음 2를 나누고, 3을 나누는 것을 고려함.
- 예시 --> `i % 3 == 0 and d[i] > d[d // 3] + 1: d[i] = d[i // 3] + 1` 



#### [1912번 연속합](https://www.acmicpc.net/problem/1912)

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/BJ/DP/BJ_1912_continuous_sum.py)

![연속합](./images/1912.PNG)



> 전략

- d[] 리스트에 `현재 값(ix : i)`과 `d[i - 1] + 현재 값` 중 큰 값을 대입
- `[1, -1, 3]`를 예로 들자면 `1`의 경우에는 초기 값이므로 `d[0] = 1`.
- `-1`의 경우에는 현재 값인 -1과 이전 ix의 d[0] + -1를 고려해 큰 값을 저장. `d[1] = 1 + (-1) = 0`
- `3`의 경우에는 현재 값인 3이 합보다 크므로 `d[2] = 3`



#### [9095번 1, 2, 3 더하기](https://www.acmicpc.net/problem/9095)

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/BJ/DP/BJ_9095_add_1_2_3.py)

![1,2,3 더하기](./images/9095.PNG)

> 전략

- bottom up방식으로, 0부터 정수 3까지의 방법 개수를 미리 구함
- `d[i] = d[i - 1] + d[i - 2] + d[i - 3]`



#### [11053번 가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053)

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/BJ/DP/BJ_11053_LIS.py)

![가장 긴 증가하는 부분 수열](./images/11053.PNG)

> 전략

- d[] 리스트에 가장 긴 부분 수열의 길이를 저장
- 과거 시점의 값이 현재 값 보다 작으면서 연속된 것이 가장 긴 것을 d[] 리스트에 저장 





#### [14002번 가장 긴 증가하는 부분 수열4](https://www.acmicpc.net/problem/14002)

[코드로 이동하기](https://github.com/yeomkyeorae/algorithm/blob/master/BJ/DP/BJ_14002_LIS_4.py)

![가장 긴 증가하는 부분 수열4](./images/14002.PNG)

> 전략

- 최대 LIS를 구하면서 이전 최대 LIS(현재 시점이 과거 어느 index로부터 연결된 것인지)를 `v`라는 배열로 저장함.
- 최대 LIS를 구하고 나서 `v`를 기반으로 tracing함