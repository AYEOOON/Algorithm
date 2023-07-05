# 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다. 
# n개의 원판을 A에서 C로 이동시키는 과정을 생각해보면 최종적으로 n-1개의 원판을 b에 놓고, 남은 하나의 원판을 A에서 C로 옮긴 후 B의 원판들을 C에 옮기면 된다.
# www.youtube.com/watch?v=FYCGV6F1NuY
# 1. 첫 번째 재귀에서는 맨 밑의 N번째 원반을 목적지로 옮기기 위해 위의 N-1 개의 원반을 경유지로 옮긴다.
# 2. 그 다음 N 번째 원반을 목적지로 옮긴다.
# 3. 경유지에 있는 N-1 개의 원반을 to로 옮긴다.
    

# 내 풀이
from sys import stdout, stdin
n = int(stdin.readline())

def hanoi(n, a, b, c):    # a는 현재 n개의 원판이 쌓여있는 곳, b는 n-1개의 원판을 옮겨 놓을 곳, c는 a에서 남은 원판을 놓을 곳이다.
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)   # n-1개의 원판을 1번 막대에서 2번 막대로 옮김
        print(a, c)    # 남은 1개의 원판을 1번 막대에서 3번 막대로 옮김
        hanoi(n - 1, b, a, c)  #  다시 n-1개의 원판을 2번 막대에서 3번 막대로 옮김
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)


# 다른사람 풀이
memo={}
def hanoi(value,start,finish,support):
        key=(value,start,finish,support)
        if key in memo:
             return memo[key]
        if value==1:
            return f"{start} {finish}"
        if value>=2:
            output= "\n".join([hanoi(value-1,start,support,finish),f"{start} {finish}",hanoi(value-1,support,finish,start)])
            memo[key] = output
            return output
        
num=int(input())
print(f"{2**num-1}")
print(hanoi(num,"1","3","2"))
