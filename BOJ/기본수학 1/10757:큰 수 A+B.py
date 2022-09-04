# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하는 문제
# 다른 언어에서는 메모리가 터져 큰 수를 입력할 수 없지만, 파이썬은 오버플로우가 없기 때문에 터지지 않는다. 


# 내 풀이

import sys
input = sys.stdin.readline

A,B = map(int,input().split())  # 값 입력

print(A+B)  # 합 출력
