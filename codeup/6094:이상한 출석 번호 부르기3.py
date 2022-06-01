# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.
# 단, 첫 번째 번호와 마지막 번호가 몇 번인지는 아무도 모른다. 음수(-) 번호, 0번 번호도 있을 수 있다.


# 내풀이
num = int(input())
a = list(map(int, input().split()))
result = a[0]    # result에 0번째 값 잆력
for i in a:
  if result > i: result = i
print (result)


# 다른 풀이
num = int(input())
numlist = map(int, input().split())

a = min(numlist)
print(a)

