# 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.
# 풀지 못한 문제
# https://velog.io/@cosmos/Programmers%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EA%B9%8C%EC%9A%B4-%EC%88%98-python


# 풀이1

def solution(array: list, n: int) -> int:
    return array[sorted([[index, abs(n-num), num] for index, num in enumerate(array)], key=lambda x: (x[1], x[-1]))[0][0]]

# 풀이2

solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]   # abs: 절댓값


# 풀이3

def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer
