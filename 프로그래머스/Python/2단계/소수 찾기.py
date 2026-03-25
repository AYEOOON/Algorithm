'''
https://school.programmers.co.kr/learn/courses/30/lessons/42839
: 한 자리 숫자가 적힌 종이 조각들이 주어진다. 이 숫자들을 조합하여 만들 수 있는 모든 숫자 중에서 소수의 개수를 구하는 문제.

[초기 접근..]
처음에는 문자열의 부분 문자열을 이용해 숫자를 만들 수 있지 않을까 생각했다. (1, 7, 17..)

하지만 문제를 다시 읽어보니 숫자의 순서를 바꿀 수 있다는 조건이 있었다. 
따라서 실제 가능한 숫자는 (1, 7, 17, 71..)이 되므로 부분 문자열 문제가 아니라 순열 문제라는 것을 알게 되었다.

[해결..]
문제 과정을 크게 3단계로 나눌 수 있다. 

1. 가능한 모든 숫자 생성
  - 숫자 길이가 1부터 len(numbers)까지의 모든 순열을 생성한다.
  - 이 과정은 itertools.permutations 를 사용하면 쉽게 만들 수 있다.
2. 중복 숫자 제거
  - 순열을 만들면 같은 숫자가 여러 번 만들어질 수 있다.
  - 따라서 set을 사용하여 중복을 제거한다.
3. 소수 판별
  - 만들어진 숫자들 중에서 소수인지 판별하여 개수를 센다.
  - 소수 판별은 2 ~ num-1 까지 나누어 떨어지는지 확인하는 방식으로 구현했다.
'''
from itertools import permutations

def solution(numbers):
    answer = 0
    nums = set()
    
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            nums.add(int(''.join(p)))
        
    for num in nums:
        if isPrime(num):
            answer += 1
            
    return answer

def isPrime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num%i == 0:
            return False
    
    return True
