# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

# 내 풀이
def solution(numbers):
    num = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i in num:
            num.remove(i)
            
    return sum(num)

# 개선한 내풀이
return sum([i for i in [1,2,3,4,5,6,7,8,9,0] if i not in numbers])


# 다른사람 풀이
def solution(numbers):
    return 45 - sum(numbers)
