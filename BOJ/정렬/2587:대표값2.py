# 다섯 개의 자연수가 주어질 때 이들의 평균과 중간값을 구하는 프로그램을 작성하시오.
# 첫째 줄부터 다섯 번째 줄까지 한 줄에 하나씩 자연수가 주어진다. 


# 내 풀이

import sys
input = sys.stdin.readline

num = []             # 변수를 저장하는 리스트 생성
for i in range(5):   # 5번 반복
  num.append(int(input()))   # 입력한 숫자를 num 리스트에 넣어줌

print(sum(num)//5)    # 평균
print(sorted(num)[2]) # 중앙값


