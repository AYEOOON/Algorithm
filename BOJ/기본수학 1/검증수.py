# 검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지이다.
# 첫째 줄에 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어진다.
# 첫째 줄에 검증수를 출력한다.

# 내 풀이
import sys
input = sys.stdin.readline

num = list(map(int, input().strip().split()))
arr = []

for i in num:
  arr.append(i**2)

print(sum(arr)%10)


# 다른 사람 풀이
print(sum(int(i)**2 for i in input().split())%10)  # input().split()는 리스트로 저장되기 때문에 가능
