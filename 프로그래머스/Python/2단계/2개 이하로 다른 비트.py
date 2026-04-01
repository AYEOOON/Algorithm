'''
https://school.programmers.co.kr/learn/courses/30/lessons/77885
: 양의 정수 x에 대해 다음 조건을 만족하는 함수 f(x)를 구하는 문제

[초기 접근]
처음에는 아래처럼 풀려고 했는데..
- 모든 수를 이진수로 변환
- x+1, x+2, ... 순차적으로 증가시키면서
- 비트 차이가 2개 이하인지 비교

이 방법은 숫자 범위가 크고, 배열의 길이가 최대 10만이기 때문에 완전 탐색은 시간 초과가 남
그래서 비트 패턴 자체를 분석하는 방향으로 접근하였다.

[풀이 방향]
짝수
- 짝수는 항상 끝 비트가 0
- +1하면 비트가 1개만 변경됨

홀수
- 홀수는 항상 끝이 1
- 오른쪽부터 1이 연속되고, 그 앞에 0이 존재
- 오른쪽에서 처음 등작하는 0을 찾음
- 그 0을 1로 바꾸고, 바로 오른쪽 1을 0으로 바꿈
'''

'''
[풀이 1]
문자열 기반
- 비트 변화를 직접 눈으로 확인할 수 있어서 이해하기 쉬움
- 하지만 문자열 변환이 포함되어 있어 성능은 상대적으로 비효율적
'''

def solution(numbers):
    answer = []
    
    for number in numbers:
        # 짝수
        if number % 2 == 0:
            answer.append(number + 1)
        
        # 홀수
        else:
            bit = '0' + bin(number)[2:]  # 앞에 0 추가
            idx = bit.rfind('0')         # 오른쪽에서 0 찾기
            
            bit = list(bit)
            bit[idx] = '1'
            bit[idx + 1] = '0'
            
            answer.append(int(''.join(bit), 2))
    
    return answer

'''
[풀이2]
xor 활용
- x ^ (x + 1) => x와 x+1의 다른 비트 위치를 모두 1로 표시
- 왜 >> 2?
  ‣ 바뀐 비트 영역에서 필요 없는 하위 2비트 제거
  ‣ 최소 변경만 남기기 위함
- x + ((x ^ (x + 1)) >> 2) + 1
  ‣ 가장 작은 증가값을 만들어서
  ‣ 조건을 만족하는 최소값 계산
'''

def solution(numbers):
    answer = []
    
    for x in numbers:
        if x % 2 == 0:
            answer.append(x + 1)
        else:
            answer.append(x + ((x ^ (x + 1)) >> 2) + 1)
    
    return answer
