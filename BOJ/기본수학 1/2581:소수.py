# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오. 

# 내 풀이
M = int(input())
N = int(input())

sosu = []
for i in range(M, N+1):
    for j in range(2, i+1):
      if j == i:
        sosu.append(i)
      if i%j == 0:
        break

if len(sosu) == 0:
  print(-1)

else:
  print(sum(sosu))
  print(min(sosu))


# 다른사람 풀이
m=int(input())
n=int(input())
l=[1]*(n+1)
l[1]=0
for i in range(2, int(n**(0.5))+1):  # 범위를 제곱근으로 줄이면 속도가 빨라진다. 
    if l[i]:
        for j in range(i*i, n+1,i):
            l[j]=0

l=[i for i in range(m,n+1) if l[i] == 1]
if sum(l)==0:
    print(-1)
else:    
    print(sum(l))
    print(min(l))
