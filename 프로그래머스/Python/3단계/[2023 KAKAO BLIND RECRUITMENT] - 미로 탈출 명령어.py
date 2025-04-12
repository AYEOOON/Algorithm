"""
n x m 격자 미로가 주어집니다. 당신은 미로의 (x, y)에서 출발해 (r, c)로 이동해서 탈출해야 합니다.

단, 미로를 탈출하는 조건이 세 가지 있습니다.

격자의 바깥으로는 나갈 수 없습니다.
(x, y)에서 (r, c)까지 이동하는 거리가 총 k여야 합니다. 이때, (x, y)와 (r, c)격자를 포함해, 같은 격자를 두 번 이상 방문해도 됩니다.
미로에서 탈출한 경로를 문자열로 나타냈을 때, 문자열이 사전 순으로 가장 빠른 경로로 탈출해야 합니다.
이동 경로는 다음과 같이 문자열로 바꿀 수 있습니다.

l: 왼쪽으로 한 칸 이동
r: 오른쪽으로 한 칸 이동
u: 위쪽으로 한 칸 이동
d: 아래쪽으로 한 칸 이동

격자의 크기를 뜻하는 정수 n, m, 출발 위치를 뜻하는 정수 x, y, 탈출 지점을 뜻하는 정수 r, c, 탈출까지 이동해야 하는 거리를 뜻하는 정수 k가 매개변수로 주어집니다.
이때, 미로를 탈출하기 위한 경로를 return 하도록 solution 함수를 완성해주세요. 
단, 위 조건대로 미로를 탈출할 수 없는 경우 "impossible"을 return 해야 합니다.
"""
"""
백트래킹으로 풀려고 했지만 시간 초과로 인해 다른 사람 풀이를 참고하여 푼 문제
그리디하게 푼 풀이
dlru순으로 명령어를 사용해야하기 때문에 앞서서 d를 최대한 사용하고, 그 다음 l을 많이 사용한다.
이후 ru를 반복해서 사용하면 된다.
1. 위 로직으로 매번 이동거리 계산 후 경로 추가
2. 현재 좌표에서 도착 좌표까지 거리와 이동할 거리가 남았다면, 위 반복

* 시작 좌표부터 도착 좌표까지의 거리와 k가 모두 동일한 홀수나, 짝수여야 이동 좌표로 도착 가능
"""

# 풀이
def remain(x, y, r, c): # 남은거리 계산 함수
    return abs(x-r) + abs(y-c)

def solution(n, m, x, y, r, c, k):
    if (k - remain(x, y, r, c)) % 2 or remain(x, y, r, c) > k:
        return "impossible"
    
    answer = ''
    move = 0

    # 아래로 최대한 이동
    while x < n and (k - move) > remain(x, y, r, c):
        move += 1
        x += 1
        answer += 'd'

    # 좌로 최대한 이동
    while 1 < y and (k - move) > remain(x, y, r, c):
        move += 1
        y -= 1
        answer += 'l'

    # 우좌로 반복 이동
    while (k - move) > remain(x, y, r, c):
        move += 2
        answer += 'rl'

    # 가야할 길로 dlru 순으로 이동 
    if x < r:
        answer += 'd' * (r-x)
        x = r
    if y > c:
        answer += 'l' * (y-c)
        y = c
    if y < c:
        answer += 'r' * (c-y)
        y = c
    if x > r:
        answer += 'u' * (x-r)
        x = r

    return answer
