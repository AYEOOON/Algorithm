# 메모리가 8MB로 제한된 상태로 N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하는 문제
# 수 정렬하기2에서 썼던 sort()를 사용하면 메모리가 초과된다.
# 수를 정렬하기 위해서는 숫자가 들어오면 그 숫자의 위치를 1씩 카운트를 하여 출력하면 된다. 
# 내 풀이

import sys    # input()을 쓰면 속도가 느려져 sys라이브러리를 호출
input=sys.stdin.readline

N = int(input()) # 수의 개수

num = [0] * 10001           # 0으로 가득찬 길이가 10000인 리스트를 생성

for _ in range(N) :
    temp = int(input())   # 입력 받는 수를 temp로 저장
    num[temp] += 1        # 해당 temp의 값을 +1씩 증가해줌

for i in range(10001) :      # 입력받는 숫자는 0부터 10000사이의 숫자만 입력받음
    if num[i] != 0 :
        for j in range(num[i]) :    # 해당 리스트를 처음부터 반복문을 돌면서 0이 아닐 경우 해당 숫자만큼 temp를 출력
            print(i)
