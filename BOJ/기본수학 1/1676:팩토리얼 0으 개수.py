# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
# 예를 들면, 10!은 3,628,800이다. 0이 아닌 숫자가 나오기 전 0의 갯수는 2개이다. 


# 내 풀이
N = int(input())
fac = 1
cnt = 0

for i in range(N, 0, -1):
  fac *= i

for j in reversed(str(fac)):
  if j == '0':
    cnt += 1
  else:
    break
print(cnt)

# 다른사람 풀이(https://hwiyong.tistory.com/360)
# 팩토리얼로 얻을 수 있는 수를 인수 분해 했을때, 0이 늘어나는 순간은 10(2x5)가 곱해지는 순간이다.
# 따라서 5의 개수를 찾으면 된다. 
N = int(input())
print(N//5 + N//25 + N//125)
