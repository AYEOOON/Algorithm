# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.


# 내 풀이

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []

for _ in range(N) :
    board.append(list(map(int, input().split())))

for i in range(N) :
    temp = list(map(int, input().split()))

    for j in range(M) :
        board[i][j] += temp[j]

for i in range(N) :
    for j in range(M) :
        print(board[i][j], end = " ")
    print()

    
# 다른사람풀이

import sys

x,y = map(int,input().split())
name = sys.stdin.read().splitlines()

a = [list(map(int,name[idx].split())) for idx in range(2*x)]
L = [[a[i][j] + a[x+i][j] for j in range(y)] for i in range(x)]

for c in L:
    print(" ".join(str(x) for x in c))
