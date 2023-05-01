# Binary Search
- 정의: 정렬된 배열에서 타겟을 찾는 검색 알고리즘
- 시간복잡도: O(log n)

### 주의 사항
- Overflow: mid pointer 계산 시, 다음과 같이 계산하는 경우 int 자료형 최대값 초과로 인해 오버플로가 발생할 수 있다.
```python
mid = (left + right) // 2
```
오버플로를 방지하기 위해서는 다음과 같이 계산하면 된다.
```python
mid = left + (right - left) // 2
# left + (right - left) / 2 = left/2 + right/2
```
