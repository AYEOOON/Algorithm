# N이 홀수라고 가정할 때, 산술평균, 중앙값, 최빈값, 범위(N개의 수들 중 최댓값과 최솟값의 차이)를 구하여라
# 산술평균은 소수점 이하 첫째 자리에서 반올림한다. 최빈값이 여러개면 최빈값 중 두번째로 작은 값을 출력한다. 
# 최빈값을 구하는 것이 가장 어려웠으며, 시간초과가 뜨지않도록 주의해야한다. 

#  내 풀이(시간초과)
n = int(input())

nums = []
for _ in range(n) :
	nums.append(int(input()))

# 산술평균
print(round(sum(nums)/n))

# 중앙값
nums.sort()
print(nums[int((n-1)/2)])

# 최빈값
counts = dict()
for i in range(1,n+1) :
	counts[i] = []

maxCount = 1
count = 1
for j in range(1,n) :
	if nums[j] == nums[j-1] :
		count += 1
	else :
		counts[count].append(nums[j-1])
		if maxCount < count : maxCount = count
		count = 1
	if j == n-1 : 
		counts[count].append(nums[j])
		if maxCount < count : maxCount = count

if n == 1 :
	counts[1].append(nums[0])

counts[maxCount].sort()
if len(counts[maxCount]) == 1 :
	print(counts[maxCount][0])
else :
	print(counts[maxCount][1])

# 범위
print(nums[-1]-nums[0])



# 다른사람 풀이(counter을 사용하여 푼 풀이)

import sys
from collections import Counter

n = int(sys.stdin.readline())

nums = []
for i in range(n):   # 입력받은 n의 수만큼 숫자 입력
    nums.append(int(sys.stdin.readline()))   # nums 리스트에 넣기

nums.sort()   # 리스트 정렬
nums_s = Counter(nums).most_common()
print(round(sum(nums) / n))   # 산술평균
print(nums[n // 2])     # 중앙값
if len(nums_s) > 1:     # 최빈값
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])
print(nums[-1] - nums[0])  # 범위
