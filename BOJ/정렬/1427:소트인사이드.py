# 정렬하려고 하는 수 n이 주어지면, 그 수의 각 자리수를 내림차순으로 정렬하는 문제


# 내 풀이

import sys
input=sys.stdin.readline

n = int(input())
nums = list(map(int,str(n)))

nums.sort(reverse = True)   # sort함수를 이용하여 list에 들어있는 숫자들을 내림차순시킨다. 

for i in nums:    # 정렬된 리스트를 한개씩 출력시킨다. 옵션으로 end=''를 주어 한줄에 출력이 되도록한다. 
  print(i,end='')

  

# 다른사람풀이

nums = input()   #
nums = [int(n)  for n in nums]

ordered_nums = sorted(nums, reverse=True)

for n in ordered_nums : 
    print(n, end="")
