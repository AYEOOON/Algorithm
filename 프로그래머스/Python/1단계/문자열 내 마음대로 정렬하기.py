# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하는 함수를 완성하세요.

# 내 풀이
# key 기준으로 정렬을 할 경우 오직 key 기준으로만 정렬을 한다. key이외의 나머지 요소에 대해선 정렬되지 않음.
# lambda를 이용한 key 설정에서 튜플을 넣어줌으로써 정렬의 우선순위를 지정할 수 있다.
def solution(strings, n):
    return sorted(sorted(strings), key=lambda x : x[n])  # sort, sorted에 key인자를 넣어줌으로써 정렬 기준을 정할 수 있다.


# 다른사람 풀이
def solution(strings, n):
    return sorted(sorted(strings), key=lambda x : x[n])  # lambda에 튜플을 넣어줌으로써 sort의 우선순위를 정할 수 있다.
    
    
