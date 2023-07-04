# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴하는 함수를 완성하는 문제

# 내 풀이
def solution(n):
    arr = list(map(int, str(n)))
    return list(reversed(arr))


# 다른사람 풀이1
def digit_reverse(n):
    return list(map(int, reversed(str(n))))


# 다른사람 풀이2
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]
  
# 1. 입력 정수를 문자열로 변환하고 
# 2. 해당 문자를 반복(for)문으로 각 문자를 다시 정수로 변환해서 list형태로 저장하고 
# 3. list에 있는 요소의 순서를 반대로 뒤집고 반전된 목록을 결과로 반환
