# 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다. 
# n개의 원판을 A에서 C로 이동시키는 과정을 생각해보면 최종적으로 n-1개의 원판을 b에 놓고, 남은 하나의 원판을 A에서 C로 옮긴 후 B의 원판들을 C에 옮기면 된다.


# 내 풀이

n = int(input())
def hanoi(n,a,b,c):
    if n == 1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)
count = 0
for _ in range(n):
    count = 2*count + 1
print(count)
hanoi(n,1,2,3)
