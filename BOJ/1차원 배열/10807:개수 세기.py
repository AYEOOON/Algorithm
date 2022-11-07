# 총 N개의 정소가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하는 문제
# 첫 째줄에 정수의 개수 N개가 주어지고, 둘째줄에는 정수가 공백으로 구분되어있다. 셋째줄에는 찾으려는 수인v가 주어진다.


# 내 풀이

import sys
input = sys.stdin.readline

N = int(input())

numlist = list(map(int,input().split()))
v = int(input())
print(numlist.count(v))


# 다른 사람 풀이

input()
print(input().split().count(input()))
