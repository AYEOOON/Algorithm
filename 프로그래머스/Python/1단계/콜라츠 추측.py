# 콜라츠 추측이란 주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다.
# 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 
#  위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요.
#  단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.

# 내 풀이
def solution(num):
    answer = 0
    if num == 1:
        return 0
    else:
        while(num != 1):
            if num%2 == 0:
                num = num//2
                answer += 1
            else:
                num = num*3+1
                answer += 1
        if answer >= 500:
            return -1
    return answer

# 개선한 내 풀이
def solution(num):
    answer = 0
    if num == 1:
        return 0
    while(num != 1):
        num = num/2 if num%2 == 0 else num*3+1   #주의!
        answer += 1
        if answer >= 500:
            return -1
    return answer


# 다른사람 풀이
def collatz(num):
    for i in range(500):   # 500번이상 반복하면 -1을 반환하게 되있으므로 그냥 500번으로 횟수 제한
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    if num == 1:
      return 0
    return -1
    
        
        
    
