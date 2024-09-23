"""
하노이 탑(Tower of Hanoi)은 퍼즐의 일종입니다. 
세 개의 기둥과 이 기동에 꽂을 수 있는 크기가 다양한 원판들이 있고, 퍼즐을 시작하기 전에는 한 기둥에 원판들이 작은 것이 위에 있도록 순서대로 쌓여 있습니다.
게임의 목적은 다음 두 가지 조건을 만족시키면서, 한 기둥에 꽂힌 원판들을 그 순서 그대로 다른 기둥으로 옮겨서 다시 쌓는 것입니다.

  1. 한 번에 하나의 원판만 옮길 수 있습니다.
  2. 큰 원판이 작은 원판 위에 있어서는 안됩니다.

하노이 탑의 세 개의 기둥을 왼쪽 부터 1번, 2번, 3번이라고 하겠습니다. 
1번에는 n개의 원판이 있고 이 n개의 원판을 3번 원판으로 최소 횟수로 옮기려고 합니다.

1번 기둥에 있는 원판의 개수 n이 매개변수로 주어질 때, n개의 원판을 3번 원판으로 최소로 옮기는 방법을 return하는 solution를 완성해주세요.
"""

# 내 풀이
def solution(n):
    answer = []
    
    def hanoi (n, a, b, c, answer):
        if n == 1:
            answer.append([a,c])
        else:
            hanoi(n-1, a, c, b,answer)
            answer.append([a,c])
            hanoi(n-1, b, a, c,answer)
        return answer
    
    return hanoi(n, 1,2,3, answer)
  

# 다른 사람 풀이
def hanoi(n):

    def _hanoi(m, s, b, d):
        if m == 1:
            yield [s, d]  # yield : 호출 안 쪽으로 프로그램 제어를 넘겨주는 키워드
        else:
            yield from _hanoi(m-1, s, d, b)
            yield [s, d]
            yield from _hanoi(m-1, b, s, d)

    ans = list(_hanoi(n, 1, 2, 3))
    return ans  # 2차원 배열을 반환해 주어야 합니다.
