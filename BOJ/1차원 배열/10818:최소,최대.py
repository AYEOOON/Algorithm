# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.


# 내 풀이
cnt = int(input())
numbers = list(map(int, input().split()))
print(min(numbers),max(numbers))


# 다른사람 풀이
import sys
input()
a = [int(s) for s in sys.stdin.read().split()]
print(min(a), max(a))
