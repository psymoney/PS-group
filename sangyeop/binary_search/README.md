# Binary Search
- 정의: 정렬된 배열에서 타겟을 찾는 검색 알고리즘
- 시간복잡도: O(log n)

### 주의 사항
- Overflow: mid pointer 계산 시, 다음과 같이 계산하는 경우 int 자료형 최대값 초과로 인해 오버플로가 발생할 수 있다. (excl. Python)
```python
mid = (left + right) // 2
```
오버플로를 방지하기 위해서는 다음과 같이 계산하면 된다.
```python
mid = left + (right - left) // 2
# left + (right - left) / 2 = left/2 + right/2
```

### 풀이 방법
1. 반복
2. 재귀
```python
def recursive(l, r, sorted_array, target) -> int:
    if l > r:
        return -1

    mid = l + (r - l) // 2

    if sorted_array[mid] == target:
        return mid
    elif sorted_array[mid] < target:
        return recursive(mid + 1, r, sorted_array, target)
    else:
        return recursive(l, mid - 1, sorted_array, target)
```
3. Python package bisect 활용
```python
import bisect

index = bisect.bisect_left(sorted_array, target)
```

4. Python operator `in`
```python
has_array_target: boolean = target in array
```
이건 `in` 연산자가 어떤 알고리즘을 사용하는지 확인이 되지 않아 시간 복잡도를 모르겠음.
GPT 선생은 sequencial 자료형에 대해서 선형 탐색을 하기에 O(N)의 시간 복잡도를 갖는다 하는데, 풀어본 문제에서 빠른 결과를 내는 코드들은 `in`을 사용하여 풀었기에 궁금증이 남는다.
[10815: 숫자카드](https://www.acmicpc.net/problem/10815) 해당 문제를 재귀 기반 이분탐색으로 풀이할 경우 1 <= N, M <= 500,000를 만족하는 N, M에 대한 시간복잡도는 O(M log N)로 풀이에 총 2,132ms 가 소요되지만, 연산자 `in`을 사용한 풀이는 288ms가 소요된다(CPython 3기준).


#### 속도 비교
bisect > 반복 > 재귀 (부등호가 더 큰 쪽이 우수)

