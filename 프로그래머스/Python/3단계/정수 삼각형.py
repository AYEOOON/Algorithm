""" 
                7
              3   8 
             8  1  0
            2  7  4  4
          4  5   2   6  5

위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 
아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 
예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.
"""


# 내 풀이
def solution(triangle):
    answer = 0
    arr = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    arr[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if arr[i-1][j] == 0:
                arr[i][j] = arr[i-1][j-1] + triangle[i][j]

            else: 
                arr[i][j] = max(arr[i-1][j-1] + triangle[i][j], arr[i-1][j]+triangle[i][j])

    return max(arr[-1])



# 다른사람 풀이
def solution(triangle):
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])


# 다른사람 풀이
"""
1. 한 층씩 제거하며, 그 층에서 계산한 최대 이동거리 배열을 계산하여 한 층을 제거한 triangle을 첫번째 input, 이동거리 배열을 두번쨰 input으로 넣음
2. 따라서 triangle이 없으면 제거할 층이 없으므로 최종 조건
3. [0]+l, l+[0]을 이용하여 모서리 조건 해결
"""
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
