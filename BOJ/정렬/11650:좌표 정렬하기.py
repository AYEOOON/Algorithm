# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한다음 출력하는 프로그림은 만드는 문제
# 점의 개수를 입력받아 x좌표를 기준으로 정렬하고 y좌표 기준으로 정렬한다.


# 내 풀이

import sys
input = sys.stdin.readline

N = int(input())   # 점의 개수
nums = []

# 입력
for _ in range(N):
  x,y = map(int,input().split())
  nums.append([x,y])

# 정렬 -> x좌표 정렬 후 y좌표 정렬
nums.sort(key = lambda x : (x[0],x[1]))   # sort를 이용하여 이차원 리스트 오름차순 만들기

# 출력
for i in range(N):
  print(nums[i][0],nums[i][1])

  
# 다른사람 풀이

import sys
def convert(s):
    x, y = s.split()
    return int(x) + int(y)/1000000
arr = sys.stdin.readlines()[1:]
arr = sorted(arr, key=lambda x: convert(x))
print(''.join(arr))
