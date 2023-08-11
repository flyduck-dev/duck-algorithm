def solution(A):
    unique_values = set(A)
    for P in range(len(A)):
        unique_values.discard(A[P])
        if not unique_values:
            return P
#    return -1

# 파이썬 set 학습 링크 : https://it-plus.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EB%B2%95-5-2-%EC%A7%91%ED%95%A9-%EC%9E%90%EB%A3%8C%ED%98%95-%EC%B4%9D%EC%A0%95%EB%A6%AC-%EC%A7%88%EB%AC%B8%EC%9C%BC%EB%A1%9C-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0

# set(A): 중복을 허용하지 않는 요소들의 집합
# set(A)는 리스트 A의 모든 고유한 요소로 구성된 세트를 생성. 배열 A의 각 요소가 최소한 한 번 이상 나타나는지 쉽게 확인할 수 있다.

# unique_values.discard(A[P]): discard 메소드는 세트에서 특정 요소를 제거. 만약 해당 요소가 세트 내에 없다면 아무 것도 하지 않는다.
# if not unique_values: 만약 unique_values 세트가 비어 있다면, 배열 A의 모든 고유한 값이 이미 검사되었다는 것을 의미.
# 따라서 현재의 P는 배열 A에서 발생하는 모든 값을 포함하는 가장 작은 인덱스

# return P: 조건이 충족되면 현재의 P 값을 반환. P는 배열의 인덱스이므로 0부터 시작하며, A[0], A[1], ..., A[P]에서 발생하는 모든 값을 포함하는 가장 작은 정수 P

# return -1: 만약 모든 요소를 순회한 후에도 unique_values 세트가 비어 있지 않다면, 함수는 -1을 반환.
