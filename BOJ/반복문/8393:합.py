# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.


a = int(input())
sum = 0       #임의로 정한 변수의 값을 0으로 지정해줌
for i in range(a+1):    #1부터 n까지의 합이라고 했으니, range의 범위는 n+1가 된다. 1부터 n까지 i에 대입
    sum = sum + i    #a에 i의 값을 누적해서 더한다.
print(sum)
