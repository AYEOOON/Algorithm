# 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다.
# 주어지는 수는 100보다 작은 자연수 또는 0이다.



# 내 풀이

import sys
input = sys.stdin.readline

board = []

for _ in range(9) :
    board.append(list(map(int, input().split())))

X = 0
Y = 0
MAX = -1

for i in range(9) :
    for j in range(9) :
        if board[i][j] > MAX :
            MAX = board[i][j]
            X = i+1
            Y = j+1

print(MAX)
print(X, Y)


# 다른사람 풀이

