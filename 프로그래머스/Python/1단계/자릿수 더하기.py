# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# 내 풀이
def solution(n):
    return sum(map(int, str(n)))    # map(f, iterable)은 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수, str(number)각 인덱스에 int()함수를 수행해서 변환 후 sum()


# 다른사람 풀이(재귀로푼 방법)
# 123을 10으로 나눈 나머지 3을 반환합니다. 123//10은 123을 10으로 나눈 몫 12를 반환합니다. 따라서 12를 다시 함수에 넣고 돌리겠죠.
# return 123%10 + sum_disgit(123//10) -> return 3 + sum_digit(12) -> return 3+2+sum_digit(1)
def sum_digit(number):
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)
