# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.

# 내 풀이
def solution(n):
    num = list(map(str, str(n)))
    return int(''.join(sorted(num, reverse=True)))

# 개선한 내 풀이
def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))  # list를 사용하지 않아도 풀수있다!


# 다른사람 풀이
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
